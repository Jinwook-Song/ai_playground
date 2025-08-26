## Company Overview
- **Name:** ABOUT YOU (ABOUT YOU SE & Co. KG / ABOUT YOU Holding SE)
- **Industry:** Fashion e‑commerce / Internet marketplace + B2B e‑commerce platform (SCAYLE)
- **Headquarters:** Hamburg (offices also in Berlin and other European markets)
- **Company size:** Scale-up / large startup — public filings & press list ~1k–1.5k employees (job context lists 500–1000+). Active customers: ~12.8–12.9M LTM (Q3 2024/2025).
- **Product footprint & reach:**
  - Consumer-facing online fashion store and app (mobile-first, heavy personalization).
  - B2B tech product: SCAYLE — enterprise shop system licensed to brands/retailers (>200 stores).
  - SCAYLE Payments — payment services arm (BaFin license, rollouts underway).
  - Catalog: hundreds of thousands of items; thousands of brands.
- **Business highlights (context):**
  - Emphasis on mobile app and personalization (app drives most revenue).
  - Mix of B2C commerce and fast-growing B2B platform business.

## Mission and Values
- **High-level mission:** "To revolutionize the shopping experience — especially for Gen Y & Z — by creating an inspiring, personalized, mobile-first shopping experience." (Corporate site messaging)
- **Cultural signals / values:**
  - Customer centricity and personalization (data-driven product feeds).
  - Fast, product-led engineering: "we always want to be first."
  - Collaboration and knowledge sharing (ABOUT YOU Tech community, AY Academy).
  - Agile, feedback-driven teams (regular retrospectives and cross-team exchange).
  - Brand/creator partnerships and "fashiontainment" — blending entertainment and commerce.
- **Engineering culture clues:** cross-functional squads, emphasis on performance and scale, knowledge sharing, and internal tech services (SCAYLE).

## Recent News or Changes
(Selected, high-impact items from public releases)
- July 11, 2025 — Zalando completed a strategic combination / voluntary takeover of ABOUT YOU (closing announced). This is a major structural change: pan‑European consolidation with potential product and org implications.
- July 1, 2025 — Regulatory clearance announced ahead of the closing (European Commission clearance).
- May 2025 — ABOUT YOU reported record FY performance (group revenue surpassed EUR 2.0 billion in FY 2024/2025) and continued customer growth; updated guidance and positive adjusted EBITDA improvements were highlighted.
- Oct 2024 — SCAYLE Payments received a BaFin payment services license and has begun rollouts in Austria/Germany, meaning tighter control over payment flows and deeper integration opportunities for marketplace features.
- 2024–2025 — Continued expansion of exclusive collaborations, new branded collections (e.g., Netflix collection) and growth in the DACH market. Ongoing focus on profitability, margin improvement, and the growth of SCAYLE’s ARR.

Implication for candidates: the company is scaling both consumer and enterprise products, investing in infrastructure (payments, SCAYLE) and undergoing strategic change from the Zalando combination — expect some re-prioritization, integration work, and emphasis on operational stability.

## Role Context and Product Involvement
Job: Senior Golang Engineer (Shop Backend) — App & Web team (Hamburg or Berlin; remote-friendly)

What the role likely sits on and who you’ll work with:
- **Team:** App & Web squad — cross-functional (backend + frontend + product + QA) focused on the App, Mobile Website and Desktop Website experiences.
- **Service / product context:** Backend API(s) that serve the App & Web frontend — `gRPC` APIs in Go that encapsulate core business logic for the shop (likely product feeds, catalog queries, personalization endpoints, cart/session APIs, pricing & promotions, and parts of order flow that feed the frontend).
- **Platform & infra dependencies:**
  - AWS hosting (EC2/EKS, managed services, ElastiCache), Terraform/CloudFormation for IaC.
  - Relational DBs (MySQL) for transactional data; Redis for caching/session/state.
  - Containerization (Docker; Kubernetes implied), CI/CD pipelines for deployments.
  - Observability stack: centralized logging, metrics, alerting (Prometheus/Grafana, ELK/CloudWatch or similar).
- **Responsibilities from job:** implement and harden gRPC Go APIs; optimize performance and response times; production hardening at scale; participate in agile ceremonies and cross-team knowledge sharing.

How this role impacts product:
- Responsible for frontend-facing latency and reliability (mobile-first experience).
- Improvements here directly influence conversion, AOV, and customer experience.
- Likely expected to contribute to service ownership, incident response, and architecture discussions.

Practical inferences about team structure and career expectations:
- Senior role: expected to be hands-on coding, design API contracts (`.proto`), optimize DB queries & caching layers, mentor others and shape API/architecture decisions.
- Close collaboration with frontend/product to provide simple APIs for UX and performance SLAs.
- Interaction with platform/SRE teams for deployment, monitoring, and incident management.

## Likely Interview Topics
Technical areas interviewers will probe (with sample focus points they care about):

1. Go (Golang) fundamentals and idioms
   - Concurrency primitives (`goroutines`, `channels`) and patterns to avoid leaks and race conditions.
   - Memory model, GC considerations and profiling (heap vs stack, pprof).
   - Error handling patterns, interfaces, composition, and dependency injection in Go.
   - Testing in Go (unit tests, table-driven tests, mocks, integration tests).

2. gRPC API design and performance
   - Designing `proto` schemas and versioning strategies.
   - Unary vs streaming RPCs, deadlines, timeouts and cancellation propagation.
   - Serialization size/CPU tradeoffs and compatibility strategies.
   - Client-side patterns (retries, load balancing) and server instrumentation.

3. Backend architecture & system design (shop-specific)
   - Designing scalable product/catalog endpoints, pagination, search vs filtered queries.
   - Caching strategies: cache invalidation, cache-aside, TTL choices, cache warming.
   - Handling promotions/price rules, A/B experiments, personalization at scale.
   - Consistency models, idempotency, race conditions around carts/orders.

4. Databases & storage
   - SQL design (MySQL) for high read throughput; indexing, query optimization, denormalization tradeoffs.
   - Redis usage for session/state/caching; eviction policies, clustering, persistence tradeoffs.
   - Data partitioning strategies and read replicas.

5. Cloud & DevOps (AWS + infra-as-code)
   - Terraform / CloudFormation patterns, state management, drift, modules.
   - Autoscaling, load balancing, IAM/security practices, network topology.
   - Runtime in containers (Docker), orchestration (Kubernetes/EKS), deployment strategies (blue/green, canary).

6. Observability & reliability
   - Metrics, SLIs/SLOs, alerting thresholds, runbooks, postmortem culture.
   - Centralized logging, distributed traces (OpenTelemetry/Jaeger), profiling in production.
   - Incident response: what to do during production degradations, RCA process.

7. Performance & optimization
   - Profiling real bottlenecks, latency budgets, tail-latency reduction strategies.
   - Benchmarking RPC endpoints and DB hotspots.
   - Bulk operations / pagination optimization for mobile apps.

8. Senior-level responsibilities & collaboration
   - Code review approach, mentoring juniors, design docs, architecture trade-offs.
   - Cross-team collaboration (frontend/product/platform) and influencing without authority.
   - Handling ambiguity during reorganizations/mergers (Zalando combination).

Behavioral and culture fit topics:
- Agile team experiences (retrospectives, continuous improvement).
- Examples of production incidents you led/participated in — learnings and follow-up.
- Knowledge sharing: talks, docs, internal training (AY Academy style).

## Suggested Questions to Ask (to surface important signals and impress interviewers)
Technical / role-fit questions
- "Can you describe the Shop Backend's service boundaries — which APIs are 'owned' by this team vs shared platform services?"
- "What are the main performance or reliability pain points today for App & Web? Any recent incidents or hotspots?"
- "What scale targets and latency SLAs should this role be focused on improving?"
- "Which observability tools do you use (metrics, tracing, logs)? How mature are your SLOs and runbooks?"
- "How is the gRPC API surface designed for frontend developers? How do you handle versioning and backward compatibility?"
- "How do you handle cache invalidation for catalog and pricing data across MySQL and Redis?"
- "What does your CI/CD and deployment cadence look like? Do teams own production deploys and rollbacks?"
- "What level of control do dev teams have over infra (Terraform, CloudFormation)? Is there a dedicated infra/SRE team?"
- "Do you use event-driven systems for eventual consistency (Kafka, SNS/SQS)? When would I use events vs direct RPC?"

Team / career / org questions
- "What's the typical squad size and structure on App & Web? Who would I work most closely with?"
- "What are the expectations for a 'Senior' engineer in the first 3–6 months?"
- "How do you measure the impact of an engineer (metrics / outcomes)?"
- "How does ABOUT YOU support upskilling (e.g., Go ramps, AY Academy, mentorship)?"

Company / change questions (showing strategic awareness)
- "How will the Zalando combination affect the tech org / product priorities for the next 6–12 months?"
- "How does SCAYLE integration or Payments rollout influence the Shop Backend roadmap?"

Practical / logistics
- "What is the interview loop and timing? Who will I meet?"
- "Is compensation banding published for this role? How does equity/bonus typically work?"
- "What is the relocation and visa support timeline and process?"
- "What's your remote/hybrid policy, and how often does the team meet in person?"

Asking these signals:
- The Zalando/SCAYLE/Payments questions show business awareness and long-term thinking.
- Observability & SLO questions show an operations-minded senior engineer.
- Questions about ownership and deployment cadence show you care about end-to-end responsibility.

Additional brief coaching for Juan (positioning & immediate prep)
- Primary gaps in the job spec vs Juan's CV:
  - Go experience: the role expects strong Go skills; Juan has strong Node.js/Express background.
  - Seniority: role asks 5+ years; Juan has ~3 years.
- How to close/mitigate gaps before interviews (quick wins):
  - Build a small Go + gRPC sample: one service with `proto` definitions, simple DB (MySQL) calls, and Redis caching. Host on GitHub and include readme with decisions.
  - Prepare 2–3 stories showing backend design scaled in Node.js (cache strategies, DB optimizations, reducing response times) and draw parallels to how you'd implement similar solutions in Go.
  - Review Go concurrency and pprof basics; prepare concrete examples for profiling and optimizing latency.
  - Prepare a system-design case for a "catalog & personalization API for mobile app" — include caching, timeouts, fallbacks and SLOs.
  - Emphasize AWS cert and real infra experience: Terraform, Docker, CI/CD, and production incident handling.
- Interview prep priorities (practical study list):
  - Go: goroutines, channels, interfaces, testing, pprof (2–3 targeted hours per topic).
  - gRPC: proto design, deadlines, streaming basics.
  - System design: catalog, cart, checkout architectures and caching patterns.
  - Observability: distributed tracing, SLO examples, common alerting mistakes.

Good answers and examples you should prepare
- One or two production incidents: what caused it, how you diagnosed (metrics/trace/logs), mitigation, and what changed (postmortem actions).
- A performance improvement you led: baseline metrics, approach (profiling, caching, DB indexing), results (numbers).
- An API design decision: tradeoffs, client ergonomics, versioning, and backward compatibility.

---
If you want, I can:
- Convert this into a 30–60 minute interview prep checklist tailored to Juan (with suggested study resources and a mock question set).
- Draft 3–4 concise stories (STAR format) from Juan's experience mapped to this role (incidents, performance wins, teamwork).