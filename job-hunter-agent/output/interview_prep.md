# Interview Prep: ABOUT YOU – Senior Golang Engineer (m/f/d) - Shop Backend

## Job Overview
- Role: Senior Golang Engineer (Shop Backend), App & Web team (Hamburg or Berlin, remote-friendly).
- Focus: Develop and production-harden a gRPC API in Go that serves ABOUT YOU’s App, Mobile Web and Desktop Web. Improve scalability, latency, and reliability of frontend-facing backend services running on AWS. Operate in cross-functional agile squads and share knowledge within ABOUT YOU Tech.
- Must-haves: Strong Go skills, 5+ years building complex backend APIs, experience with relational DBs (MySQL), Redis, cloud/container tooling (AWS, Terraform/CloudFormation, Docker/K8s), observability & SRE mindset.
- Impact: This role directly affects conversion and UX by reducing latency and increasing reliability of user-facing endpoints (catalog, pricing, personalization, cart-related services).

## Why This Job Is a Fit (for Juan)
- Domain match: Juan has e‑commerce backend experience (admin dashboard + platform work) and has directly shipped features for product/catalog/checkout flows — aligns well with Shop Backend responsibilities.
- Infrastructure alignment: He has hands-on AWS experience (certified), Docker, CI/CD, MySQL/Postgres tuning, and Redis caching — all central to the role.
- Behavioral & team fit: Experience working in Agile teams, retrospectives, and cross-functional collaboration aligns with ABOUT YOU culture.
- Gaps and mitigation:
  - Go: Juan’s production backend experience is in Node.js/Python; explicit Go experience is limited. This is the primary technical gap but is highly bridgeable with a focused ramp (see tactical actions below).
  - Seniority: Role asks 5+ years vs Juan’s ~3. Counterbalance by highlighting impact, ownership examples, breadth of responsibilities, and rapid learning evidence (AWS cert, project ownership).

Short pitch Juan should use: "I bring production backend experience for e‑commerce — database tuning, Redis caching, AWS deployments and performance work — plus a strong track record of shipping customer-facing APIs. I’m rapidly ramping in Go (sample repo + tests) and ready to apply my system-design and operational experience to reduce latency and harden the Shop Backend API."

## Resume Highlights for This Role (Snapshot)
Focus on top bullets to emphasize in the interview — say these first, then expand with stories.

- Backend ownership & scale
  - Owned backend API development at TechSolutions Madrid for apps serving 10k+ users.
  - Implemented REST APIs consumed by web & mobile, collaborating closely with frontends to optimize UX.
- Performance & DB expertise
  - Reduced page load times ~30% via query tuning, indexing, and schema changes.
  - Implemented Redis caching strategies to decrease API response times and backend load.
- Production and deployment
  - Built CI/CD pipelines (GitHub Actions), Docker-based deployments; deployed services on AWS.
  - AWS Certified Developer — demonstrates cloud operational knowledge.
- E‑commerce relevance
  - Contributed to e‑commerce platform: product management, checkout flows, and an admin dashboard with real-time analytics.
- Soft skills & processes
  - Agile ceremonies, code reviews, postmortems, and cross-functional collaboration.

Quick positioning line for interview intros: "I’m a backend engineer with e‑commerce experience focused on improving API performance and reliability through DB optimization, Redis caching, and well-automated deployments. I’ve led production improvements and I’m actively ramping in Go and gRPC."

## Company Summary (Product, Values, Context)
- What ABOUT YOU does:
  - Mobile-first fashion e‑commerce platform with heavy personalization; also builds SCAYLE, a B2B commerce platform and Payments capabilities.
- Values & engineering culture:
  - Product-led, fast-moving teams; emphasis on personalization, mobile experience, cross-functional squads, knowledge sharing (AY Academy).
  - Engineering metrics and performance matter; expect responsibility for SLAs, instrumentation, and production ownership.
- Business context:
  - Rapid scaling + strategic combination with Zalando (July 2025) — expect refocus on integration, efficiency, and operational stability.
  - Investments in payments and SCAYLE imply platform-standardization and possibly shared infra/services.
- Why that matters for the role:
  - Systems must meet strict latency/reliability targets for mobile users; cross-team coordination likely with SCAYLE/Payments/platform teams.

## Predicted Interview Questions
(Organize responses: explicit statement → approach → example/metrics)

Technical — Go & gRPC
- "Explain Go's concurrency model and how you'd prevent goroutine leaks in a long-running gRPC server."
- "How do you approach error handling and dependency injection in Go?"
- "Walk me through designing a gRPC .proto for a product/catalog read API. How do you handle versioning and backward compatibility?"
- "How do you profile a Go service in production to find CPU and memory bottlenecks? Which tools and metrics do you use?"
- "When would you choose streaming vs unary RPCs in gRPC for frontend/backends?"

Technical — Backend & System Design
- "Design a scalable catalog API for mobile app use: requirements, caching, pagination, SLOs, and data freshness constraints."
- "How would you implement cache invalidation for product price and stock changes to ensure near-real-time accuracy with high read volume?"
- "Describe approaches to reduce tail latency for a critical API endpoint."
- "How would you design idempotent cart update operations to handle retries from the mobile client?"

Databases & Caching
- "Show how you would optimize slow SQL queries on MySQL under high read load (indexes, denormalization, read replicas)."
- "Explain Redis eviction strategies and how you’d pick TTLs and cache layering (cache-aside, write-through)."

Cloud/DevOps & Observability
- "How would you structure Terraform modules for a microservice with RDS, ElastiCache, and EKS resources?"
- "Describe your approach to SLOs/SLIs for an API and how you'd tune alerting to avoid noise."
- "Walk me through an incident you handled: detection, mitigation, communication, and the postmortem."

Behavioral / Leadership
- "How have you mentored junior engineers or driven knowledge sharing in your team?"
- "Tell me about a time you disagreed with a design decision. How did you handle it?"
- "Given the Zalando combination and organizational changes, how would you handle shifting priorities?"

Questions likely to probe Juan's gaps (anticipate):
- "What Go projects have you built? Show code, tests, and explain choices." — Have a small repo ready.
- "Given the 5+ years senior bar, what leadership or architecture decisions have you led?" — Prepare examples showing impact beyond feature delivery.

## Questions to Ask Them (curated & strategic)
Technical / role-fit
- "Which specific Shop Backend APIs does this squad own? Which services are shared platform responsibilities?"
- "What are the current top performance or reliability pain points for App & Web? Any recent incidents I should know about?"
- "What latency SLAs / SLOs are you targeting for critical mobile endpoints?"
- "Which observability stack do you use (metrics, tracing, logs)? How mature are your SLOs and runbooks?"
- "Do teams write and own Terraform modules, or is infra centralized? How do you manage IaC drift and state?"

Team & career
- "What does success look like in months 1, 3 and 6 for a Senior Engineer joining this squad?"
- "Typical squad size and composition? Who will I collaborate with daily (frontend/product/SRE)?"
- "How is mentorship and technical growth supported (AY Academy, training budgets)?"

Company context (shows strategic thinking)
- "How is the Zalando/ABOUT YOU integration shaping tech priorities for the Shop Backend?"
- "How do SCAYLE and Payments roadmaps interact with the App & Web team?"

Practical / logistics
- "What is the interview loop, and who will I meet?"
- "What's the relocation/visa process and typical timeline?"
- "What is the expected on-site cadence for remote-friendly roles?"

Use the questions above selectively — pick 4–6 based on the interviewer (recruiter vs tech lead vs manager).

## Concepts To Know/Review (concrete list + action items)
Prioritize 8–12 focused items with suggested quick-study actions. Allocate study time: 2–3 focused days pre-interview (intense) or 1 week if you have more time.

1. Go fundamentals (2–4 hours)
   - Goroutines, channels, race conditions, defer, interfaces.
   - Error handling idioms, context.Context propagation.
   - Action: follow a 1–2 hour Go tutorial and implement simple CLI.

2. gRPC basics and designing .proto (1–2 hours)
   - Unary vs streaming, deadlines/timeouts, metadata and error codes.
   - Action: create a tiny gRPC service + client with a proto for catalog read.

3. Profiling & performance in Go (1–2 hours)
   - pprof CPU/heap profiles, benchmarking, tracing integration.
   - Action: run pprof on a simple app; interpret flame graphs.

4. System design: Catalog & Shop APIs (3–4 hours)
   - Data models, caching strategy, pagination, read-replicas, eventual consistency, SLOs.
   - Action: sketch a 20-minute whiteboard design for a catalog API.

5. MySQL optimization (1–2 hours)
   - Index selection, EXPLAIN, query refactor, read replicas, denormalization patterns.

6. Redis strategies (1 hour)
   - Cache-aside vs write-through, eviction policies, clustering, persistence tradeoffs.

7. AWS basics & infra-as-code (1–2 hours)
   - RDS/ElastiCache, EKS/ECS basics, Terraform module patterns, IAM security practices.

8. Observability & SRE practices (1–2 hours)
   - SLIs/SLOs, runbooks, alert fatigue, distributed tracing (OpenTelemetry/Jaeger).

9. Incident & postmortem examples (prep 2 stories)
   - Prepare 1–2 STAR stories of incidents: detection → mitigation → postmortem actions.

10. Translate Node.js experience to Go (prep examples)
   - Map caching, DB tuning, and CI/CD patterns you used in Node to how you'd implement in Go.

Suggested concrete deliverable before interview:
- Small GitHub repo: Go + gRPC microservice that reads from MySQL and caches with Redis. Include README explaining choices, profiling notes, and tests. This will show initiative and directly answer the "show Go code" question.

## Strategic Advice (Tone, Focus Areas, Red Flags & How to Handle Gaps)

Tone & framing
- Be confident about what you know; be explicit about the gap and show rapid mitigation.
  - Example: "I have three years of backend experience in Node.js and Python and an AWS Developer certification. I’ve been ramping in Go and built a small gRPC service to demonstrate idiomatic usage — here’s the repo."
- Use outcome-focused metrics: whenever possible, quantify improvements (latency %, traffic reduction, MTTD/MTTR improvements).
- Emphasize ownership and product impact: how your changes affected conversion or user behavior.

Focus areas during the interview
- Latency & reliability: show you know how to measure, profile, and reduce tail latency.
- Caching & data freshness: give concrete strategies for cache invalidation with examples.
- Production hardening: describe health checks, graceful shutdowns, circuit breakers, retries with exponential backoff, rate limiting.
- Observability: talk about realistic SLOs and how those drive engineering decisions.
- Collaboration: describe how you partnered with frontend/product to craft API contracts and acceptable fallbacks for degraded backends.

How to handle the Go gap (script)
- Honest, quick acknowledgement: "I haven’t used Go in production X years, but I’ve shipped backend services in Node/Python with identical operational demands."
- Pivot to proof: "I built a Go + gRPC sample service (link) and can walk you through tradeoffs, concurrency model decisions, and pprof output."
- Bridge with concrete parallels: map patterns you used (e.g., connection pooling, prepared statements, cache-aside) and show how they transfer to Go idioms.

How to handle the seniority gap (script)
- Focus on impact and breadth: describe cross-functional work, decisions you own, mentoring, architectural input.
- Offer to own a high-impact project in first 90 days (e.g., reduce response time for X endpoint by Y%).

Red flags to watch out for (and questions to ask if you see them)
- Red flag: No clarity on SLOs/SLA, observability or runbooks — ask about metrics and incident ownership.
- Red flag: Teams can't deploy independently or are blocked by central ops — ask about infra ownership and deployment cadence.
- Red flag: High churn in team or constant re-prioritization due to acquisitions — ask about product stability and roadmap clarity.
- Red flag: No plan for Go on-boarding or expectations of immediate mastery — clarify ramp expectations and available learning support (AY Academy).

Negotiation and logistics cues
- Visa/relocation: ABOUT YOU offers visa support — ask specifics early if relocation is relevant.
- Compensation: If recruiter asks for expectations, express interest pending a full understanding of role responsibilities and level; ask for band.
- Remote policy: Confirm hybrid rhythm and on-site expectations for Hamburg/Berlin.

## Tactical Interview Preparation Plan (48–72 hour sprint)
Day 1
- Quick Go crash course (3 hours): syntax, goroutines, channels, context.
- Build minimal gRPC service skeleton (2 hours): proto + simple CRUD handler returning mock data.

Day 2
- Integrate MySQL + Redis to the service (2–3 hours): implement a cache-aside read and SQL query with index; add simple tests.
- Add pprof endpoints and run a quick CPU/heap profile (1 hour).
- Prepare 3 STAR stories (1 hr): incident, performance improvement (DB/Redis), cross-functional API design.

Day 3
- System design mock (2 hours): design catalog API on whiteboard; prepare SLOs, caching, fallbacks.
- Rehearse answers to top 8 predicted questions (1–2 hours) with quantifiable metrics.
- Prepare questions to ask them (pick 6) and refine intro pitch (30 min).

Deliverables to bring to interview:
- GitHub link to the small Go/gRPC service + README and notes.
- 2–3 printed bullet points for STAR stories.
- A concise one-page design sketch for the catalog API.

## Example STAR Stories (short outlines Juan should expand)
1. Performance improvement (DB + Cache)
   - Situation: Product pages slow at peak.
   - Task: Reduce API latency for catalog reads.
   - Action: Ran EXPLAIN on slow queries, added indexes and query refactor; added Redis cache-aside for most-read endpoints; added monitoring to track cache hit rate.
   - Result: 30% page load time reduction, backend CPU down X%, fewer DB slow queries; documented approach and added metrics dashboard.

2. Production incident & postmortem
   - Situation: API outage due to DB replica lag causing timeouts.
   - Task: Restore availability and diagnose root cause.
   - Action: Rolled back feature, increased connection limits to replicas, promoted healthy read replica, implemented circuit-breaker and graceful degradation for non-critical queries; authored postmortem with action items.
   - Result: Restored service in 25 minutes, MTTR improved; added automated monitoring for replica lag and a runbook for failover.

3. Cross-functional API design
   - Situation: Frontend needed a simpler product listing endpoint with pagination and personalization.
   - Task: Design API contract minimal for mobile and support personalization without heavy coupling.
   - Action: Designed API with cursor pagination, precomputed personalization keys, defined fallbacks, ran contract review with frontend/product.
   - Result: Faster implementation for frontend, 20% improvement in time-to-first-render for mobile.

## Closing: How to leave interviewers impressed
- Lead with impact and evidence: start answers with a one-sentence outcome, then show the approach and metrics.
- Demonstrate operational maturity: mention runbooks, SLOs, observability tools you used and how they guided decisions.
- Show learning momentum: present the Go/gRPC repo, explain three technical choices you made, and show pprof/demo screenshots if possible.
- Ask high-signal questions that show product, infra and strategic awareness (Zalando merger, SCAYLE/Payments interplay, SLAs).

---

If you want, I can:
- Draft 3–4 full STAR answers from Juan’s experience mapped to top interview questions.
- Convert the Tactical Preparation Plan into a timed 60–90 minute mock-interview and feedback script.
- Produce a short README template for the Go/gRPC sample repo you should push to GitHub.

Good luck — focus on demonstrating system-level thinking, measurable impact, and your readiness to ramp in Go quickly while owning end-to-end service reliability.