#!/usr/bin/env python3
import os
import struct
import sys
import zlib

SUFFIXES = ('.png', '.jpg', '.jpeg')
SKIP_DIRS = {'.git', 'node_modules', 'dist', '.astro', '__pycache__'}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHANNELS = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}


def png_problem(data):
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        return 'not a PNG (bad signature)'
    pos = 8
    ihdr = None
    idat = bytearray()
    end = False
    while pos + 8 <= len(data):
        (declared,) = struct.unpack('>I', data[pos:pos + 4])
        kind = data[pos + 4:pos + 8]
        available = len(data) - pos - 12
        if declared > available:
            name = kind.decode('latin1', 'replace')
            return (f'{name} chunk declares {declared} bytes but only {available} remain: '
                    f'file is truncated ({len(data)} bytes on disk)')
        body = data[pos + 8:pos + 8 + declared]
        if kind == b'IHDR':
            ihdr = body
        elif kind == b'IDAT':
            idat += body
        elif kind == b'IEND':
            end = True
            break
        pos += 12 + declared
    if ihdr is None:
        return 'no IHDR chunk'
    if not idat:
        return 'no IDAT chunk'
    if not end:
        return f'no IEND chunk: file is truncated ({len(data)} bytes on disk)'
    if len(ihdr) < 13:
        return 'IHDR chunk is too short'
    width, height, depth, colour, _comp, _filt, interlace = struct.unpack('>IIBBBBB', ihdr[:13])
    if colour not in CHANNELS:
        return f'unsupported PNG colour type {colour}'
    try:
        raw = zlib.decompress(bytes(idat))
    except zlib.error as exc:
        return f'image data does not decompress: {exc}'
    if interlace == 0:
        row = (width * CHANNELS[colour] * depth + 7) // 8
        expected = (row + 1) * height
        if len(raw) != expected:
            return (f'image data decodes to {len(raw)} bytes, expected {expected}: '
                    f'only the top {100 * len(raw) // expected}% of the image is present')
    return None


def jpeg_problem(data):
    if data[:2] != b'\xff\xd8':
        return 'not a JPEG (missing SOI marker)'
    if data[-2:] != b'\xff\xd9':
        return f'no EOI marker at the end: file is truncated ({len(data)} bytes on disk)'
    return None


def problem_for(path):
    data = open(path, 'rb').read()
    if path.lower().endswith('.png'):
        return png_problem(data)
    return jpeg_problem(data)


def main():
    failures = []
    checked = 0
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            if not name.lower().endswith(SUFFIXES):
                continue
            path = os.path.join(base, name)
            rel = os.path.relpath(path, ROOT)
            checked += 1
            problem = problem_for(path)
            if problem:
                failures.append((rel, problem))
            else:
                print(f'ok   {rel}')
    print()
    if failures:
        for rel, problem in failures:
            print(f'FAIL {rel}: {problem}')
        print(f'\n{len(failures)} of {checked} image assets are corrupt.')
        print('A browser renders a truncated image partially and reports no error,')
        print('so a corrupt asset ships silently and only shows up as a visual bug.')
        return 1
    print(f'{checked} image assets decode cleanly.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
