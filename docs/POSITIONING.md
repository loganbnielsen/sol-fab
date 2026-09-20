# Sol Fabricator — Website Positioning & IA

**Status:** approved 2026-09-20 · v1.0 · source of truth for the website.

**The rule:** every product claim on the site must trace to evidence in `../sol`. If it
doesn't, it doesn't ship. This keeps the site a description of the product that exists,
rather than the one we intend to build.

---

## 1. Core promise

**H1 (approved):**

> Run a production backend without a platform team.

**Why this over the alternatives.** "One engineer. A whole production backend." is
punchier but overstates the scope. The real thesis is more interesting: application
engineers should not need a second specialization — or a second team — just to get
software into production.

**Description (title/meta):**

> Sol Fabricator turns your backend code into a production system — builds,
> infrastructure, deployment, observability, and operations included.

**Brand line (kept separate from the promise):**

> *Make production boring again.*

The promise opens the page; the brand line closes it. They do different jobs and must not
compete for the H1.

**Scope boundary (must ship alongside the promise):** "without a platform team" means *no
dedicated platform/DevOps specialization*, for a small engineering organization, on
single-region Kubernetes. It does not mean "no expertise required" and does not mean "any
scale". Sol "productizes DevOps expertise, not engineering judgment"
(`docs/architecture/PRODUCT_ARCHITECTURE.md`).

---

## 2. Hierarchy of distinctiveness

One promise, three pillars, four supporting proofs.

**Promise:** no platform team.

**Three pillars** — *how* the promise is true. Each owns a homepage section:

1. **Local is production-shaped.** Same Helm charts, same service DNS, same security
   model as production — the only difference is scale. "It worked locally" predicts
   production.
2. **Infrastructure is a build artifact.** Deployment, wiring, and observability are
   derived from the application, not hand-authored per environment.
3. **Operations are built in.** Observability, status, release inspection, rollback, and
   failure diagnosis are one workflow, not a stack you assemble.

**Four supporting proofs** — credibility, not headline:

4. One contract, two languages — OCaml (deepest path) and TypeScript (on-ramp).
5. Typed events are the only cross-domain contract; teams never share code.
6. Your cloud, your infrastructure — FOSS substrate, cloud-agnostic Kubernetes, no
   proprietary runtime.
7. Evidence over magic — published real-cloud qualification runs, Kubernetes-level failure
   diagnosis, release inspection, logs that outlive the terminal.

**Agent-legibility is a proof point, not a pillar.** Sol's conventions are regular enough
that coding agents can reason about a workspace (`README.md`). Keep it as a consequence of
convention over configuration — "…and agents can operate it too" — not as a headline. Do
not position Sol primarily as an AI devtool; promote it only if it becomes demonstrably
load-bearing.

---

## 3. Homepage narrative

| # | Section | Job |
|---|---|---|
| 1 | Hero | Promise, description, honest quickstart, alpha status |
| 2 | **Local → production** | The spine: *"It worked locally" should mean something.* |
| 3 | **Infrastructure is a build artifact** | *How* that consistency is possible |
| 4 | The application model | Primitives + runtime/application contract |
| 5 | Own your cloud | Kubernetes target, AWS/GCP (experimental), direct/GitOps, escape hatches, no lock-in |
| 6 | Observability & operations | Wired in, then operated with evidence |
| 7 | Proof | Real-cloud qualification runs, dogfood, honest status |
| 8 | Close | *Make production boring again.* + CTAs |

Two ordering rules: the local → production spine sits **immediately after the hero**, and
"infrastructure is a build artifact" follows it as the explanation — not the other way
round.

---

## 4. Claims and evidence

Every row must resolve to something real in `../sol`.

| Claim | Evidence |
|---|---|
| Run a production backend without a platform team | `ROADMAP.md` — "a small engineering organization can run production systems without dedicated platform engineers"; `PRODUCT_ARCHITECTURE.md` — "DevOps expertise, not engineering judgment" |
| Local is production-shaped | `PRODUCT_ARCHITECTURE.md` — "same Helm charts used in production… the only difference is scale"; `TUTORIAL.md` — "same service DNS names, same security model" |
| Fast inner loop | `TUTORIAL.md` — `sol local run`: one `dune build`, native processes, no image rebuild |
| Infrastructure is a build artifact | `PRODUCT_ARCHITECTURE.md` — "Generated infrastructure is a build artifact"; `ROADMAP.md` — "Infrastructure is derived from code structure, not written by hand" |
| Same contract local → AWS/GCP | `Sol_cli_env_target` — `Local_k3d`, `Customer_k8s_direct`, `Customer_k8s_gitops`, `Sol_hosted`, over one deployment plan |
| Observability built in | `ROADMAP.md` Phase 3 auto-wiring; `framework/ocaml/sol-obs` facade |
| Operate with evidence | `sol status` Kubernetes diagnosis; `Sol_cli_release_inspection`; `.sol/runs/<run-id>/`; `sol rollback`; Argo Rollouts progressive delivery |
| One contract, two languages | `README.md`; `@sol-fab/kafka`, `@sol-fab/obs` |
| Typed events, no shared code | `README.md` / `PRODUCT_ARCHITECTURE.md` application model |
| Your cloud, no proprietary runtime | FOSS substrate (Kubernetes, Strimzi, Argo CD, Prometheus, Loki, Grafana, Terraform); `sol cloud plan/apply/destroy` |
| Qualified on real cloud | `docs/qualification/` run records |
| Legible to agents | `README.md` — conventions regular enough for AI coding agents |

---

## 5. Claims we are not making yet

| Not claiming | Why | Instead |
|---|---|---|
| "5 minutes to production" | Sol's own acceptance bar is **ten minutes** (`ROADMAP.md` Phase 5) and excludes prerequisite install; cloud provisioning adds Terraform time. Treat five minutes as a **measured benchmark to earn** | **"a running, observable service on your machine in minutes"** — local only |
| Multi-region / "global" | `LIVE_DEV_DEPLOY_ROADMAP.md` — "Not Yet: active-active multi-region" | "single-region Kubernetes today" |
| Production-stable | Pre-alpha (`CHANGELOG.md`, `README.md`) | Keep the alpha status strip |
| Hosted product / instant URLs | Hosted control plane never built; hosted executor removed 2026-06-22 | Omit (or "in development" if a waitlist is wanted) |
| "Any language" | TypeScript compatibility is `staged — not qualified` (`docs/deployment/compatibility.md`) | "OCaml is the deepest path; TypeScript is the on-ramp" |
| Managed cloud like a PaaS | `sol cloud` is experimental, live-tested against AWS | Label AWS/GCP provisioning experimental |
| "You don't need to *know* Terraform, Helm, or Kubernetes" | Sol removes the writing/maintaining work, not the value of understanding the underlying systems — and elsewhere we say it removes specialization, not engineering judgment | **"You don't need to write or maintain Terraform, Helm charts, or Kubernetes manifests."** |
| Enterprise features (RBAC, SSO, audit, billing) | Future hosted scope only | Omit |

---

## 6. Hero copy

> **(eyebrow)** Open-source software factory
>
> # Run a production backend without a platform team.
>
> Sol turns your backend code into a production system — builds, infrastructure,
> deployment, observability, and operations included. Run it locally on the same stack as
> production, then deploy the same contract to Kubernetes in your own cloud.
>
> **[Get started →]** **[Read the tutorial]**
>
> ● Pre-alpha · v0.1.0-alpha · not production-stable · Roadmap ↗

Quickstart terminal (real commands):

```
sol local infra up
sol new workspace myapp
cd myapp && sol up
✓ k3d cluster: redpanda · postgres · loki · grafana
✓ charge_svc deployed · worker consuming events
✓ curl localhost:8080/health → ok
```

Hero feature strip carries supporting facts, not the pillars: Open source (Apache-2.0, your
infrastructure) · OCaml or TypeScript · Evidence over magic.

---

## 7. Homepage vs. later pages

Not built yet — recorded so homepage sections stay liftable.

| Page | Owns |
|---|---|
| `/` | Promise, three pillars, the spine, primitives overview, own-cloud overview, ops overview, proof teaser, CTA |
| `/why` | Pillars in depth: typed events, one way to do things, security on day 1, escape hatches, comparisons |
| `/docs` | Curated tutorial + concepts (`contract/runtime.md`, `substrate.md`) + deploy/observability/escape-hatch guides + CLI reference generated from the CLI |
| `/proof` | Qualification run records, dogfood reports, current limitations |
| `/roadmap` | Public subset of `ROADMAP.md`, experimental vs done |

---

## 8. The local → production spine

The page's central visual, and the strongest answer to "what makes Sol different":

> **"It worked locally" should mean something.**

```
sol local run          sol up                    sol deploy
─────────────────      ──────────────────        ──────────────────
Fast inner loop   →    Production-shaped    →    Your real cloud
native processes       real containers           AWS / GCP
one dune build         real cluster              any Kubernetes

                  SAME APPLICATION CONTRACT
```

Design intent: one artifact/contract flowing left → right across three environments of
increasing realism, captioned by the parity claim. This becomes a named concept that docs
can link to.

---

## 9. Open items

- **Agent-legibility:** proof point for now; revisit promotion if it becomes load-bearing.
- **Five-minute first experience:** make it a measured benchmark, then claim it.
- **Wording:** H1 and hero copy are implemented as specified; refine from in-browser review.
