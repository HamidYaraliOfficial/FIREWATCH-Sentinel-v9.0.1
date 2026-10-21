#!/usr/bin/env python3
"""Generate FIREWATCH Pro's curated standards register and operational checklist.

The controls are original paraphrased assessment prompts, not reproductions of
proprietary/full standards. Update the source definitions here, then regenerate.
"""
from __future__ import annotations
import csv, json, re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "standards"
AS_OF = "2026-10-15"

# id, title, version/status, relationship, applicability, official/reference URL, use / caveat
FRAMEWORKS = [
("OWASP_ASVS","OWASP Application Security Verification Standard","5.0.0 (stable)","direct","Web applications and APIs","https://owasp.org/www-project-application-security-verification-standard/","Technical application-security verification baseline; checklist maps relevant families and is not a verbatim full ASVS export."),
("OWASP_WSTG","OWASP Web Security Testing Guide","v4.2 (current stable)","direct","Web application security testing","https://owasp.org/www-project-web-security-testing-guide/v42/","Testing methodology and test-family reference; some tests require accounts, code access, specialist tools, or manual validation."),
("OWASP_TOP10","OWASP Top 10","2025 (released)","direct","Web application risk awareness","https://owasp.org/projects/top-ten","Risk-awareness taxonomy; not a complete test suite or certification standard."),
("OWASP_API","OWASP API Security Top 10","2023","direct","REST, GraphQL and other APIs","https://owasp.org/www-project-api-security/","API risk taxonomy; BOLA, authentication, property/function authorization, resource use, SSRF, inventory and unsafe API consumption require contextual tests."),
("OWASP_CHEATSHEETS","OWASP Cheat Sheet Series","Rolling community guidance","supporting","Implementation and remediation guidance","https://cheatsheetseries.owasp.org/","Practical guidance, not a certifiable standard; use topic-specific current sheets."),
("OWASP_SAMM","OWASP Software Assurance Maturity Model","2.2.0 (project-listed)","supporting","Secure SDLC and organization maturity","https://owaspsamm.org/model/","Maturity model for governance, design, implementation, verification and operations; primarily evidence/interview based."),
("OWASP_MASVS","OWASP Mobile Application Security Verification Standard","Current project edition; verify at assessment time","conditional","Only if native/hybrid mobile clients are in scope","https://mas.owasp.org/MASVS/","Mobile-app standard; a web-only scan cannot establish mobile conformance."),
("OWASP_MASTG","OWASP Mobile Application Security Testing Guide","Rolling project content","conditional","Only for mobile apps and their platform interactions","https://mas.owasp.org/MASTG/","Mobile testing methodology; requires binaries/devices/source in many cases."),
("OWASP_LLM","OWASP Top 10 for LLM Applications","2025","conditional","Only where LLM/GenAI features or agents exist","https://genai.owasp.org/llm-top-10/","AI-specific risk awareness, including prompt injection, data disclosure, supply chain, poisoning, output handling and excessive agency."),
("OWASP_ATWA","OWASP Automated Threats to Web Applications","2023 project edition / verify current project page","supporting","Public-facing signup, checkout, scraping and sensitive flows","https://owasp.org/www-project-automated-threats-to-web-applications/","Bot/automation-abuse guidance; detection often needs business telemetry and product owner input."),
("OWASP_CLOUD_NATIVE","OWASP Cloud-Native Application Security Top 10","Project material marked interim/under review","adjacent","Cloud-native, container, orchestration and microservice deployments","https://owasp.org/projects/cloud-native-application-security-top-10","Use as supplemental guidance only, not as a stable compliance baseline."),
("NIST_800_115","NIST SP 800-115","2008 (published guide; check errata/current context)","supporting","Planning/conduct/reporting of technical security tests","https://csrc.nist.gov/pubs/sp/800/115/final","Assessment methodology; it explicitly is not a complete organization-wide testing program."),
("NIST_SSDF","NIST SP 800-218 Secure Software Development Framework","1.1","supporting","Software supplier and secure SDLC","https://csrc.nist.gov/pubs/sp/800/218/final","Process controls for producing and maintaining secure software."),
("NIST_CSF","NIST Cybersecurity Framework","2.0","supporting","Organization-wide cyber risk governance","https://www.nist.gov/cyberframework","Outcome taxonomy across Govern, Identify, Protect, Detect, Respond and Recover; not a prescriptive checklist by itself."),
("NIST_800_53","NIST SP 800-53 Security and Privacy Controls","Rev. 5 + current errata","supporting","Enterprise controls, especially government/high assurance","https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final","Large control catalog; this checklist maps broad families, not every control enhancement."),
("NIST_800_63","NIST SP 800-63 Digital Identity Guidelines","Revision 4 (2025)","supporting","Identity proofing, authentication and federation; especially relevant government systems","https://csrc.nist.gov/pubs/sp/800/63/4/final","Use the applicable 63A/63B/63C volume and assurance level; web observation alone cannot prove conformance."),
("NIST_PRIVACY","NIST Privacy Framework","1.0","supporting","Privacy risk and PII processing","https://www.nist.gov/privacy-framework","Voluntary privacy risk framework; does not itself establish legal compliance."),
("NIST_AI_RMF","NIST AI Risk Management Framework","1.0","conditional","Systems using AI/ML in consequential or user-facing workflows","https://www.nist.gov/itl/ai-risk-management-framework","AI lifecycle risk-management support; combine with a suitable use-case profile."),
("NIST_AI_GENAI","NIST AI RMF Generative AI Profile","1.0","conditional","GenAI/LLM systems","https://www.nist.gov/itl/ai-risk-management-framework","AI-specific supplementary risk practices; not a web scanner test suite."),
("NIST_800_61","NIST SP 800-61 Incident Response","Rev. 3 (2025)","supporting","Security incident response program","https://csrc.nist.gov/pubs/sp/800/61/r3/final","Incident response practices integrated with cybersecurity risk management."),
("ISO27001","ISO/IEC 27001","2022","supporting","ISMS and organization-wide security governance","https://www.iso.org/standard/27001","Requires organizational context, risk treatment, audit and management-system evidence; tool results cannot imply certification."),
("ISO27002","ISO/IEC 27002","2022","supporting","Information-security control guidance","https://www.iso.org/standard/75652.html","Control guidance supporting selection/implementation of information-security controls."),
("ISO27034","ISO/IEC 27034-1 Application Security","2011; reviewed/confirmed current in 2022","direct","Application security lifecycle","https://www.iso.org/standard/44378.html","Application-security concepts and lifecycle guidance."),
("ISO27017","ISO/IEC 27017 Cloud Security Controls","2026 edition","conditional","Cloud service providers and customers","https://www.iso.org/standard/27017","Cloud-specific allocation of responsibilities; applicability depends on cloud model and contract."),
("ISO27701","ISO/IEC 27701 Privacy Information Management","2025 edition","conditional","PII controllers/processors needing a privacy management system","https://www.iso.org/standard/27701","Privacy management system; cannot be concluded from external scanning alone."),
("ISO27035","ISO/IEC 27035-1 Incident Management","2023","supporting","Incident handling and lessons learned","https://www.iso.org/standard/78973.html","Process guidance covering preparation, detection, reporting, response and lessons learned."),
("ISO29147","ISO/IEC 29147 Vulnerability Disclosure","2018; reviewed/confirmed current in 2024","supporting","Vulnerability disclosure processes","https://www.iso.org/standard/72311.html","Coordinated disclosure policy and communications; applicable to product vendors."),
("ISO30111","ISO/IEC 30111 Vulnerability Handling","2019; reviewed/confirmed current in 2025","supporting","Internal product-vulnerability handling","https://www.iso.org/standard/69725.html","Process for receiving, assessing, prioritizing and resolving potential vulnerabilities."),
("ISO31000","ISO 31000 Risk Management","2018; reviewed/confirmed current in 2023","supporting","Enterprise risk management","https://www.iso.org/standard/65694.html","General risk-management guidelines, not a security testing specification."),
("GDPR","EU General Data Protection Regulation","Regulation (EU) 2016/679, as applicable/current consolidated text","conditional","Personal data processing within GDPR territorial/material scope","https://eur-lex.europa.eu/eli/reg/2016/679/oj","Conditional legal mapping; legal counsel/DPO must determine applicability and lawful basis. This checklist is not legal advice."),
("NIS2","EU NIS2 Directive","Directive (EU) 2022/2555; national transposition applies","conditional","Entities/sectors covered by applicable national implementation","https://eur-lex.europa.eu/eli/dir/2022/2555/oj","Scope depends on sector, size, jurisdiction and national transposition."),
("DORA","EU Digital Operational Resilience Act","Regulation (EU) 2022/2554","conditional","Financial entities and relevant ICT third-party arrangements","https://eur-lex.europa.eu/eli/reg/2022/2554/oj","Conditional sectoral requirements; validate legal scope and detailed RTS/ITS obligations."),
("PCI_DSS","PCI DSS","v4.0.1","conditional","Environments in scope for payment account data","https://www.pcisecuritystandards.org/document_library/","Use official PCI SSC documents and a qualified assessor as applicable; scan output does not prove PCI compliance."),
("HIPAA","HIPAA Security Rule","Current U.S. HHS rule and guidance","conditional","Covered entities/business associates handling ePHI in U.S. scope","https://www.hhs.gov/hipaa/for-professionals/security/index.html","Conditional legal/regulatory scope; consult HIPAA specialists."),
("SOC2","AICPA Trust Services Criteria / SOC 2","Current licensed criteria; verify with AICPA","conditional","Organizations seeking SOC 2 examination","https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services","SOC 2 is an examination/reporting engagement, not a product certification; criteria text may be licensed."),
("WCAG22","W3C Web Content Accessibility Guidelines","2.2 W3C Recommendation","adjacent","User-facing web interface accessibility","https://www.w3.org/TR/WCAG22/","Accessibility, not a cybersecurity standard; automated checks cover only part of success criteria."),
("EN301549","ETSI EN 301 549 accessibility requirements for ICT","Use current applicable edition","conditional","Public-sector/regulated ICT accessibility requirements, particularly Europe","https://www.etsi.org/standards","Check applicable edition and local procurement/legal obligations."),
("OPENAPI","OpenAPI Specification","3.2.1 current published line","direct","REST API contract discovery and linting","https://spec.openapis.org/oas/","Contract validity is separate from runtime authorization/security."),
("JSON_SCHEMA","JSON Schema","2020-12 family; verify dialect declared by API","supporting","JSON payload/schema validation","https://json-schema.org/specification","Schema validation does not prove authorization or business logic correctness."),
("HTTP_RFC9110","IETF RFC 9110 HTTP Semantics","2022, current with subsequent RFC updates","direct","HTTP methods, status codes, fields and semantics","https://www.rfc-editor.org/rfc/rfc9110.html","Protocol semantics; related companion RFCs may apply."),
("TLS_RFC8446","IETF RFC 8446 TLS 1.3","2018, current specification with updates","direct","TLS handshake and protocol configuration","https://www.rfc-editor.org/rfc/rfc8446.html","Pair with current TLS best-current-practice guidance and operational constraints."),
("TLS_BCP","IETF RFC 9325 and updates including RFC 9852","RFC 9852 (July 2026) updates BCP 195","direct","TLS usage policy","https://www.rfc-editor.org/rfc/rfc9852.html","New protocols using TLS must require TLS 1.3; deployed compatibility profiles still need context-specific assessment."),
("HSTS_RFC6797","IETF RFC 6797 HTTP Strict Transport Security","2012; use with current browser behavior","direct","HTTPS-only browser policy","https://www.rfc-editor.org/rfc/rfc6797.html","Validate HSTS header semantics and deployment preconditions."),
("OAUTH_RFC9700","IETF RFC 9700 OAuth 2.0 Security BCP","2025","conditional","OAuth 2.0 authorization servers and clients","https://www.rfc-editor.org/rfc/rfc9700.html","OAuth-specific configuration and flow testing requires endpoints, clients and role-aware test accounts."),
("JWT_RFC8725","IETF RFC 8725 JWT Best Current Practices","2020","conditional","Systems that issue or consume JWTs","https://www.rfc-editor.org/rfc/rfc8725.html","JWT parsing/validation behavior requires application or authorization-server context."),
("OIDC","OpenID Connect Core","1.0 with errata; verify current spec set","conditional","Federated authentication using OpenID Connect","https://openid.net/specs/openid-connect-core-1_0.html","Redirect URI, nonce, state, issuer, audience and token validation need flow-level tests."),
("PKCE_RFC7636","IETF RFC 7636 PKCE","2015","conditional","OAuth authorization-code clients where applicable","https://www.rfc-editor.org/rfc/rfc7636.html","Use current OAuth security BCP alongside PKCE."),
("COOKIE_RFC6265","IETF RFC 6265 HTTP State Management Mechanism","2011; track successor work","direct","Cookies and session state","https://www.rfc-editor.org/rfc/rfc6265.html","Browser cookie controls evolve; use current browser/platform behavior too."),
("CSP_W3C","W3C Content Security Policy Level 3","Living/current published spec; check status at use time","direct","Browser resource execution and policy","https://www.w3.org/TR/CSP/","Policy presence alone does not establish resistance to all script injection."),
("SRI_W3C","W3C Subresource Integrity","W3C specification","direct","Integrity of eligible third-party static assets","https://www.w3.org/TR/SRI/","Does not protect all dynamic resources or script supply-chain paths."),
("SARIF","OASIS SARIF","2.1.0 + Approved Errata 01","direct","Machine-readable scanner findings","https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html","Validate schema, rule metadata, locations and redaction before export."),
("CYCLONEDX","CycloneDX SBOM / supply-chain specification","1.7 (ECMA-424)","supporting","Software bill of materials and components/services","https://cyclonedx.org/specification/overview/","Generate real BOM from resolved build artifacts/tools; declared requirements-only inventory is not a complete SBOM."),
("SPDX","SPDX Software Package Data Exchange","3.x specification family; pin schema in production","supporting","SBOM and software licensing metadata","https://spdx.dev/specifications/","Select a specific schema version and validate SPDX output against its official schema."),
("SLSA","Supply-chain Levels for Software Artifacts","1.2 (approved)","supporting","Build integrity, provenance and supply-chain assurance","https://slsa.dev/spec/v1.2/","Claims require builder/source provenance evidence; not established by a local test count."),
("OPENSSF_SCORECARD","OpenSSF Scorecard","Rolling checks","supporting","Open-source repository and workflow hygiene","https://openssf.org/scorecard/","Objective repository checks; not a full secure software audit."),
("CWE_TOP25","MITRE CWE Top 25","2025","supporting","Weakness taxonomy for design/code review","https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25","Use as prioritization taxonomy; not all weaknesses can be discovered from black-box web scanning."),
("CAPEC","MITRE CAPEC","Current catalog","supporting","Attack-pattern taxonomy and threat modeling","https://capec.mitre.org/","Use to structure threat models and test ideas, not as evidence of exploitability."),
("ATTACK","MITRE ATT&CK","Current enterprise/mobile/cloud knowledge bases","supporting","Threat-informed detection/use-case coverage","https://attack.mitre.org/","ATT&CK is an adversary behavior knowledge base, not a web-app compliance standard."),
("CVSS","FIRST Common Vulnerability Scoring System","4.0","supporting","Technical severity communication","https://www.first.org/cvss/v4.0/","When publishing CVSS, provide the score and vector; do not relabel heuristic risk scores as CVSS."),
("EPSS","FIRST Exploit Prediction Scoring System","Rolling daily model","supporting","Prioritization of known CVEs with exploit-likelihood estimate","https://www.first.org/epss/","Requires CVE matching and current EPSS data; not a vulnerability severity score."),
("CISA_KEV","CISA Known Exploited Vulnerabilities Catalog","Rolling catalog","supporting","Prioritize known exploited software CVEs","https://www.cisa.gov/known-exploited-vulnerabilities-catalog","Requires inventory/CVE matching; do not assert a web finding is KEV-listed without a CVE match."),
("CIS_CONTROLS","CIS Critical Security Controls","v8.1","supporting","Organizational baseline/security program","https://www.cisecurity.org/controls/v8-1","Broad safeguard mapping; applicability depends on IG, asset class and organizational context."),
("CIS_BENCHMARKS","CIS Benchmarks","Product-specific rolling editions","conditional","OS, cloud, containers, Kubernetes, database and platform hardening","https://www.cisecurity.org/cis-benchmarks","Use only the benchmark for the exact product/version; requires authorized configuration access."),
("CISA_SECURE_BY_DESIGN","CISA Secure by Design Pledge","Voluntary pledge","supporting","Software manufacturers and product security practices","https://www.cisa.gov/securebydesign","Voluntary, not a legal certification; assess published measurable goals when applicable."),
("FIPS1403","FIPS 140-3 Cryptographic Module Validation","2019 standard, CMVP program","conditional","When validated cryptographic module requirement applies","https://csrc.nist.gov/pubs/fips/140-3/final","Application-level use of a crypto library does not establish that a deployed module is validated."),
("ISO42001","ISO/IEC 42001 AI Management System","2023","conditional","Organizations operating AI systems and seeking an AI management system","https://www.iso.org/standard/81230.html","Organization-level AI management system; conditional on AI use and desired assurance."),
("SLSA_PROVENANCE","in-toto / provenance attestations","Current specification ecosystem","supporting","Software build attestations and artifact supply-chain","https://in-toto.io/","Require cryptographically verifiable provenance tied to immutable artifacts/builders."),
]

# Domain, title, verification mode, priority default, applicability default,
# framework IDs, controls. Controls are original implementation-neutral checklist prompts.
DOMAINS = [
("GOV","Governance, authorization and scope","manual_review","P0","core",["OWASP_WSTG","NIST_800_115","NIST_CSF","ISO27001","ISO31000","CIS_CONTROLS"],[
"Obtain written authorization covering target owners, domains, IP ranges, ports, environments, test dates and permitted methods.",
"Maintain a signed scope register with explicit inclusions, exclusions, emergency contacts and approval expiry.",
"Require explicit authorization acknowledgement before any scan job can enter the active queue.",
"Define prohibited actions including destructive writes, credential attacks, denial of service and production data mutation.",
"Document third-party hosting, CDN, SaaS and processor permissions before testing their assets.",
"Set an approved testing window, time zone, notification path and stop condition for each engagement.",
"Record the business owner, technical owner, tester, reviewer and incident contact for every assessment.",
"Define an escalation workflow for suspected critical exposure or accidental sensitive-data discovery.",
"Use least-privileged, dedicated test identities and never request production user passwords.",
"Retain evidence of scope approval and any scope-change authorization in an auditable location.",
"Define data handling, retention, deletion and report-sharing terms before collection begins.",
"Review legal/regulatory restrictions and regional data-transfer requirements before scanning.",
"Record target ownership verification and resolve ambiguous host ownership before testing.",
"Re-confirm scope when DNS, hosting, domain ownership or target environment changes materially.",
"Define criteria for pausing or terminating a scan due to instability, rate-limit signals or owner request.",
"Document accepted risks with rationale, approver, compensating controls and expiration date.",
"Separate assessment permissions from production administration permissions.",
"Document the assessment methodology, coverage limits, assumptions and known blind spots.",
"Require independent review for high-impact findings and major scope exceptions.",
"Keep a record of assessment start/end times, configuration, tool version and operator identity.",
]),
("RISK","Risk assessment and threat modeling","interview_or_evidence","P1","core",["OWASP_ASVS","OWASP_SAMM","NIST_CSF","NIST_800_53","ISO27001","ISO31000","CAPEC","ATTACK"],[
"Maintain current system context, trust boundaries, data flows and external dependencies.",
"Identify security objectives, business-critical workflows and unacceptable impacts.",
"Record trust boundaries between browser, API, backend, data stores, third-party services and admin paths.",
"Threat-model authentication, authorization, uploads, webhooks, file processors and URL-fetching features.",
"Include abuse cases, insider misuse, automation/bot abuse and account/tenant takeover scenarios.",
"Track assumptions and unresolved questions in the threat model with owners and review dates.",
"Map important threats to defensive controls, tests, evidence and remediation tickets.",
"Review threat models after major architecture, identity, data-flow or third-party changes.",
"Use a documented risk method that distinguishes impact, likelihood, confidence and business context.",
"Prioritize reachable, exploitable and business-critical exposures rather than relying only on raw severity.",
"Identify crown-jewel data and the controls required around it.",
"Review failure modes caused by partial outages, dependency failures and degraded security controls.",
"Assess multi-tenant boundaries and cross-tenant impact explicitly.",
"Assess supply-chain and build pipeline threats in addition to runtime threats.",
"Record residual risk decisions and verify that compensating controls are operational.",
"Maintain a mapping from threat scenarios to ATT&CK/CAPEC where it adds actionable context.",
]),
("ASSET","Asset inventory and attack-surface discovery","automated_passive","P1","core",["OWASP_WSTG","OWASP_ASVS","OWASP_TOP10","OWASP_API","NIST_CSF","CIS_CONTROLS"],[
"Inventory in-scope hosts, ports, schemes, applications, APIs and known environment variants.",
"Discover links, forms, scripts, resources, route hints and API specifications within scope.",
"Record HTTP method, path template, parameters, content type and observed authentication context per endpoint.",
"Identify production, staging, administrative, partner and legacy API versions separately.",
"Parse robots.txt and sitemap as discovery hints without treating either as authorization to test.",
"Track endpoint source (HTML, JavaScript, OpenAPI, browser observation, manual seed) and discovery timestamp.",
"Deduplicate URL and endpoint variants using canonicalization rules documented in the tool.",
"Detect technology indicators with confidence and avoid treating a banner as proof of version or vulnerability.",
"Flag stale, undocumented, deprecated and duplicate APIs for owner review.",
"Compare current and prior inventories to identify newly exposed routes and assets.",
"Respect scope at every redirect, subresource, script-discovered URL and browser request.",
"Exclude sensitive token/reset/signature query URLs from normal crawling and report output.",
"Record discovery limits when authentication or JavaScript runtime access is unavailable.",
"Review exposed source maps, debug paths and metadata without attempting unauthorized repository access.",
"Confirm all discovered third-party hosts are separately approved before any active request is sent.",
]),
("ARCH","Secure architecture and application design","manual_review","P1","core",["OWASP_ASVS","OWASP_SAMM","OWASP_TOP10","NIST_SSDF","NIST_800_53","ISO27034","ISO27001"],[
"Document secure architecture decisions and security-relevant design trade-offs.",
"Apply deny-by-default and least privilege across application layers and service identities.",
"Keep authorization decisions server-side and independent from client-visible UI state.",
"Separate public routes, privileged administrative interfaces and internal service endpoints.",
"Define service-to-service trust and authenticate internal calls rather than trusting network position alone.",
"Avoid placing secrets, security decisions or privileged business rules in client-side code.",
"Use explicit data ownership and tenant-context propagation across service boundaries.",
"Define safe error behavior and failure modes for unavailable identity, authorization and policy services.",
"Design idempotency and replay protections for actions with financial or irreversible effects.",
"Design rate, quota and resource controls around business operations and expensive code paths.",
"Review use of caches, reverse proxies and CDNs for private or tenant-specific content leakage.",
"Use a secure-by-default configuration and require explicit opt-in for risky capabilities.",
"Document security boundaries around webhooks, URL previewers, importers and export generators.",
"Review cryptographic design and key lifecycle before implementing custom cryptography.",
"Record threat model and abuse-case review approvals before high-risk features go live.",
]),
("AUTHN","Authentication, identity lifecycle and federation","manual_review","P0","core",["OWASP_ASVS","OWASP_WSTG","OWASP_TOP10","NIST_800_63","NIST_800_53","ISO27002","OAUTH_RFC9700","OIDC","PKCE_RFC7636"],[
"Use secure authentication protocols and avoid bespoke password/token schemes.",
"Require multi-factor authentication for privileged and high-risk accounts where appropriate.",
"Protect password reset and account recovery with short-lived, single-use, purpose-bound tokens.",
"Prevent account enumeration through consistent responses and timing where feasible.",
"Apply rate limits and abuse controls to login, registration, recovery, OTP and verification endpoints.",
"Store passwords using a current, purpose-built password hashing scheme with suitable work factors and salts.",
"Reject breached or policy-prohibited credentials according to risk and organizational policy.",
"Protect authentication responses against caching and accidental token disclosure.",
"Rotate or invalidate sessions after login, privilege change, password reset and other security events.",
"Ensure logout and administrative revocation invalidate server-side state where required.",
"Validate issuer, audience, signature, expiry and intended use for JWTs and other assertions.",
"Reject algorithm confusion, key substitution and unsigned token acceptance.",
"Use exact registered redirect URI matching for OAuth redirect-based flows.",
"Use state and nonce protections appropriate to the selected OAuth/OIDC flow.",
"Require PKCE for applicable authorization-code clients and reject downgrade behavior.",
"Prevent open redirects from leaking authorization codes or tokens.",
"Protect refresh tokens with rotation or sender constraint when supported by the architecture.",
"Implement account lifecycle controls for provisioning, deprovisioning, lockout and recovery.",
"Use re-authentication or step-up checks for sensitive actions and changes to security settings.",
"Document intended assurance levels for identity proofing, authenticators and federated login.",
]),
("AUTHZ","Authorization, tenancy and object-level access","manual_review","P0","core",["OWASP_ASVS","OWASP_WSTG","OWASP_TOP10","OWASP_API","NIST_800_53","NIST_800_63","CWE_TOP25"],[
"Enforce server-side authorization on every protected object, function and property access.",
"Test horizontal access between two users with distinct, controlled test data.",
"Test vertical access across low-privilege, privileged and administrative roles.",
"Test tenant isolation across list, detail, search, export, report and bulk operations.",
"Verify object ownership and tenant context are derived from trusted server-side identity, not request parameters alone.",
"Apply field-level authorization to sensitive response properties and writable fields.",
"Prevent mass assignment of role, owner, tenant, approval, price or internal status fields.",
"Ensure hidden endpoints and client-side route guards are not treated as authorization controls.",
"Validate authorization before performing any state-changing side effect.",
"Check authorization for asynchronous jobs, exports, webhooks, file downloads and generated reports.",
"Ensure authorization context cannot be confused across concurrent requests or shared caches.",
"Define and test service-account permissions, API scopes and administrative boundaries.",
"Review group/role inheritance and deny/allow precedence for least privilege.",
"Test direct object identifiers only with authorized test accounts and non-sensitive fixtures.",
"Record expected-versus-actual outcomes and sanitized evidence for every authorization test.",
"Treat automated role-difference results as review candidates until object ownership and business context are verified.",
"Confirm default policy for unknown roles, missing claims and malformed authorization context is deny.",
"Re-test authorization after role, tenant, API schema or route changes.",
]),
("SESSION","Session, cookies and browser state","automated_passive","P1","core",["OWASP_ASVS","OWASP_WSTG","OWASP_CHEATSHEETS","COOKIE_RFC6265","OWASP_TOP10","NIST_800_63"],[
"Set Secure on session cookies in HTTPS deployments.",
"Set HttpOnly on cookies that do not require direct JavaScript access.",
"Choose SameSite deliberately based on application flows and CSRF threat model.",
"Use cookie prefixes and path/domain constraints where they add enforceable protection.",
"Avoid unnecessarily broad cookie Domain and Path scope.",
"Rotate identifiers after authentication and privilege changes.",
"Enforce idle and absolute session expiration appropriate to data sensitivity.",
"Invalidate server-side sessions on logout, revocation and account compromise events.",
"Protect state-changing requests with CSRF defenses appropriate to the authentication model.",
"Check Origin/Referer or equivalent request provenance where appropriate, without treating it as the only CSRF control.",
"Do not cache authenticated sensitive pages publicly or across tenants.",
"Ensure tokens are not exposed in URLs, browser history, referrers, telemetry or error pages.",
"Avoid storing high-value session secrets in localStorage when safer alternatives meet the architecture.",
"Review concurrent session handling and suspicious-session revocation.",
"Test session behavior in a real browser for applicable SameSite and cross-origin interactions.",
]),
("INPUT","Input validation, output encoding and injection","manual_or_specialist_tool","P0","core",["OWASP_ASVS","OWASP_WSTG","OWASP_TOP10","OWASP_CHEATSHEETS","CWE_TOP25","CAPEC"],[
"Validate inputs with allowlists, type constraints, canonicalization and size limits at trusted boundaries.",
"Use context-appropriate output encoding for HTML, attributes, JavaScript, CSS and URL contexts.",
"Use safe DOM APIs and avoid interpreting untrusted strings as executable markup or script.",
"Use parameterized database queries or equivalent safe query construction.",
"Review SQL, NoSQL, LDAP, XPath and search-query construction for interpreter injection.",
"Use safe process APIs without shell interpolation for operating-system operations.",
"Review template rendering to ensure untrusted data cannot become executable template syntax.",
"Disable unsafe XML external entity and external resource resolution where not required.",
"Validate file paths after canonicalization and enforce containment within an approved directory.",
"Validate URL-fetch inputs against scheme, hostname, port, DNS and network policy to reduce SSRF risk.",
"Prevent HTTP parameter pollution and duplicate-parameter ambiguity in security-sensitive inputs.",
"Set maximum request, header, body, nesting, decompression and parser sizes.",
"Validate Unicode, null byte, control character and alternate-encoding edge cases.",
"Ensure validation and authorization occur on the server for every input path.",
"Use safe deserialization formats and reject unexpected polymorphic/object types.",
"Avoid dynamic code evaluation and unsafe expression-language execution on user-controlled content.",
"Review regular expressions and parsing logic for catastrophic backtracking or algorithmic complexity.",
"Test reflected parameter canaries as observations only; require safe context validation before declaring XSS.",
"Confirm error messages do not echo raw dangerous input or secrets into executable output contexts.",
"Record tests requiring active payloads as manual/specialist-tool tasks rather than silently claiming coverage.",
]),
("API","API contracts, REST, GraphQL and RPC","automated_readonly","P0","core",["OWASP_API","OWASP_ASVS","OWASP_WSTG","OPENAPI","JSON_SCHEMA","HTTP_RFC9110"],[
"Maintain an authoritative API inventory with owners, versions, environments and deprecation state.",
"Validate OpenAPI documents against the declared supported specification version and schema.",
"Declare authentication and security requirements at the appropriate API/operation levels.",
"Check for operations accidentally marked public where authentication is expected.",
"Document request and response schemas, constraints, error formats and sensitive fields.",
"Apply object-level authorization to endpoints accepting object identifiers.",
"Apply function-level and property-level authorization to API operations and data fields.",
"Limit page size, batch count, query complexity, upload size and expensive operations.",
"Use quotas/rate limits and abuse protections for business-sensitive or expensive API workflows.",
"Disable or restrict introspection/schema exploration according to documented GraphQL policy.",
"Control GraphQL depth, alias count, batching and query cost when exposed to untrusted clients.",
"Validate GraphQL resolver authorization independently of schema visibility.",
"Authenticate and authorize WebSocket, SSE, gRPC and other non-REST channels where present.",
"Handle content types, methods, CORS preflight and unsupported methods consistently.",
"Prevent undocumented debug, legacy and shadow API versions from remaining unnecessarily accessible.",
"Validate webhook signatures, replay windows, source authenticity and event authorization.",
"Validate response filtering so internal fields, tokens and cross-tenant data are not exposed.",
"Version API security behavior and define compatible deprecation/removal policy.",
"Treat API discovery as inventory evidence, not proof that every business operation has been tested.",
"Use test accounts and synthetic records for destructive or state-changing business API verification.",
]),
("WEB","HTTP, browser policies and web configuration","automated_passive","P1","core",["OWASP_ASVS","OWASP_WSTG","OWASP_TOP10","HTTP_RFC9110","HSTS_RFC6797","CSP_W3C","SRI_W3C"],[
"Redirect HTTP to HTTPS without loops or downgrade paths for production sites.",
"Apply an HSTS policy only after HTTPS coverage and subdomain implications are understood.",
"Deploy a CSP appropriate to the application and avoid unsafe directives when feasible.",
"Review frame-ancestors or equivalent clickjacking protections for sensitive interfaces.",
"Set X-Content-Type-Options to prevent MIME sniffing where applicable.",
"Set a Referrer-Policy consistent with privacy and functional requirements.",
"Set Permissions-Policy to disable unused sensitive browser capabilities where feasible.",
"Review COOP, COEP and CORP where cross-origin isolation/resource isolation is required.",
"Ensure security headers are consistently applied on success, error, authentication and redirect responses.",
"Avoid leaking server/framework versions and internal host names in response banners.",
"Review cache-control behavior for authenticated and sensitive pages.",
"Ensure security-sensitive redirects use allowlisted destinations and safe URL parsing.",
"Check content-type correctness and avoid returning active content from untrusted upload hosts.",
"Ensure error pages do not expose stack traces, configuration, paths or personal data.",
"Review CORS origins, credential flags, methods and allowed headers against explicit business requirements.",
"Do not reflect arbitrary Origin values into access-control headers.",
"Use SRI for eligible immutable third-party scripts/styles and review update/rotation processes.",
"Avoid mixed content and insecure resource references in HTTPS pages.",
]),
("CRYPTO","Cryptography, certificates and secret management","automated_passive","P0","core",["OWASP_ASVS","OWASP_WSTG","OWASP_TOP10","NIST_800_53","ISO27002","TLS_RFC8446","TLS_BCP","FIPS1403"],[
"Disable obsolete TLS versions and weak cipher suites according to current platform guidance.",
"Prefer TLS 1.3 and maintain a documented compatibility exception for any TLS 1.2 dependency.",
"Validate certificate chain, hostname, expiration, validity dates and renewal ownership.",
"Protect private keys and signing keys from source code, logs, images and user-facing artifacts.",
"Use a managed secret store with access controls, rotation and audit for production secrets.",
"Separate development, staging and production keys and credentials.",
"Define cryptographic key creation, distribution, rotation, revocation, backup and destruction processes.",
"Use vetted cryptographic libraries and avoid custom algorithms or ad hoc modes.",
"Protect sensitive data in transit and at rest based on data classification and threat model.",
"Use authenticated encryption or approved constructions when encrypting application data.",
"Review random number generation and token generation for cryptographic suitability.",
"Ensure password hashes use a dedicated password-hashing scheme, not general-purpose hashes alone.",
"Prevent tokens and secrets from appearing in query strings, referer headers, telemetry and reports.",
"Define handling for certificates, signing keys and API tokens exposed in browser-delivered assets.",
"Use validated cryptographic modules only when FIPS or another validation requirement explicitly applies.",
"Monitor certificate/key expiry and test renewal before production expiry dates.",
"Test secure failure behavior when key management or cryptographic services are unavailable.",
"Record TLS settings and certificate chain evidence with time, hostname and scanner version.",
]),
("DATA","Data protection, privacy and retention","manual_review","P1","core",["OWASP_ASVS","NIST_PRIVACY","NIST_800_53","ISO27701","GDPR","HIPAA","PCI_DSS"],[
"Maintain data inventory and classification for personal, payment, authentication and business-sensitive information.",
"Minimize personal and sensitive data collected, returned, logged and retained.",
"Document data purpose, legal basis and retention requirements where privacy law applies.",
"Limit access to personal and regulated data by role, purpose and tenant.",
"Mask or redact sensitive data in logs, telemetry, error pages, exports and security reports.",
"Verify deletion and retention processes for user records, exports, backups and derived artifacts.",
"Ensure exports and downloadable reports enforce authorization and expire or revoke access when needed.",
"Use pseudonymization or aggregation in test fixtures wherever practical.",
"Avoid production personal data in ordinary development/test environments.",
"Document processor/subprocessor roles, hosting locations and international transfers where applicable.",
"Provide mechanisms for data-subject requests where legally required and applicable.",
"Assess privacy risks for new high-risk processing and document DPIA decisions where required.",
"Protect report files at rest and use a defined retention/deletion window.",
"Prevent secrets or high-sensitivity evidence from being included in analytics by default.",
"Define rules for handling accidental exposure of credentials, health records, payment data or other sensitive evidence.",
"Review response bodies and browser storage for unintended data disclosure with authorized accounts.",
]),
("FILES","Uploads, downloads, parsing and SSRF surfaces","manual_or_specialist_tool","P1","conditional",["OWASP_ASVS","OWASP_WSTG","OWASP_API","OWASP_CHEATSHEETS","CWE_TOP25"],[
"Allowlist upload types using content inspection in addition to user-supplied extension and MIME type.",
"Limit file size, count, decompression ratio, nesting depth and processing time.",
"Store untrusted uploads outside executable web roots with restrictive permissions.",
"Generate server-side storage names and prevent path traversal through supplied file names.",
"Scan or sandbox risky content before downstream use when justified by the threat model.",
"Prevent uploaded active content from sharing a trusted origin with authenticated application pages.",
"Set safe Content-Disposition and content types for file downloads.",
"Authorize file access independently of guessed or enumerated file identifiers.",
"Validate archive extraction against path traversal, symlink escape and zip-bomb behavior.",
"Disable unsafe XML external entity and external schema fetching in parsers that do not need them.",
"Use outbound request allowlists and egress network controls for URL-fetching functions.",
"Resolve and validate DNS/IP destinations at connection time to mitigate SSRF and rebinding.",
"Block loopback, link-local, private, multicast and metadata-service destinations unless explicitly required and isolated.",
"Limit redirects, schemes, ports, response sizes and timeouts in URL fetchers.",
"Use safe parsers for image, document, PDF and media processing; isolate high-risk converters.",
]),
("BUSINESS","Business logic, automation abuse and resource limits","manual_review","P1","conditional",["OWASP_WSTG","OWASP_API","OWASP_ATWA","OWASP_TOP10","NIST_CSF","ISO31000"],[
"Define expected state transitions and reject illegal workflow transitions server-side.",
"Test price, quantity, discount, tax, currency and rounding rules with synthetic accounts/data.",
"Use idempotency controls for retryable payment, order, provisioning and sensitive transaction APIs.",
"Ensure approval steps cannot be skipped by direct API calls or altered client state.",
"Define rate, quota and concurrency limits for account creation, recovery, search and expensive workflows.",
"Detect and mitigate scraping, credential stuffing, scalping, fake-account creation and resource hoarding where relevant.",
"Prevent replay of signed requests, webhooks, invitations and one-time actions beyond allowed windows.",
"Verify workflow ownership and role authorization across every step, not just entry pages.",
"Test abuse of cancellations, refunds, coupons, referral credits and trial/entitlement logic with test fixtures.",
"Ensure race conditions cannot bypass balance, stock, quota or approval invariants.",
"Document business-sensitive actions that require human review, step-up authentication or additional telemetry.",
"Avoid high-volume or destructive tests on production; use staging and owner-approved synthetic datasets.",
"Check that expensive endpoints have bounded compute, result sizes and database work.",
"Record business-owner validation for candidate risks that cannot be judged from HTTP response behavior alone.",
"Define bot detection controls with privacy review and documented false-positive handling where applicable.",
]),
("ERROR","Error handling, logging, detection and response","manual_review","P1","core",["OWASP_TOP10","OWASP_ASVS","OWASP_WSTG","NIST_800_61","NIST_CSF","NIST_800_53","ISO27035"],[
"Return generic client-facing errors while preserving useful, access-controlled server diagnostics.",
"Never log passwords, access tokens, session identifiers, private keys or unredacted authorization headers.",
"Log security-relevant authentication, authorization, privilege, configuration and administrative events.",
"Protect logs against unauthorized access, tampering, truncation and uncontrolled retention.",
"Use reliable timestamps/time synchronization and correlate events across services.",
"Alert on high-risk events and define response ownership and escalation timeframes.",
"Test alert delivery and incident response with safe tabletop exercises.",
"Maintain incident response procedures for credential exposure, data leakage and critical vulnerability discovery.",
"Document evidence-preservation and chain-of-custody practices for investigations.",
"Define how security findings are classified, assigned, tracked, accepted and closed.",
"Test that log contents are sanitized against CR/LF and structured-log injection.",
"Separate operational logs from security audit events where required by assurance needs.",
"Use monitoring to detect abnormal rates, unusual role changes and suspicious business workflows.",
"Maintain response playbooks for scanner-induced instability and accidental out-of-scope requests.",
"Record lessons learned and feed root causes back into secure design and regression tests.",
]),
("SDLC","Secure development lifecycle and verification","interview_or_evidence","P1","core",["OWASP_SAMM","OWASP_ASVS","NIST_SSDF","NIST_CSF","ISO27034","ISO27001","CISA_SECURE_BY_DESIGN"],[
"Define a documented secure development lifecycle that covers requirements, design, implementation, verification, release and operations.",
"Train developers and reviewers on relevant vulnerability classes and secure patterns.",
"Require peer review and risk-based security review before merging sensitive changes.",
"Use code analysis and secret detection in CI for relevant repositories.",
"Run unit, integration, API contract and security regression tests in CI.",
"Require tests for vulnerability fixes and security-relevant incident root causes.",
"Establish security acceptance criteria for high-risk features before implementation.",
"Keep security exceptions traceable, time-bound and approved by an accountable owner.",
"Run threat modeling for significant design changes and external integrations.",
"Separate build, test and release privileges and restrict CI tokens to least privilege.",
"Protect build and deployment workflows from untrusted pull-request code execution.",
"Pin third-party actions and build dependencies to immutable versions/identifiers where feasible.",
"Use isolated, ephemeral and access-limited build agents for release pipelines.",
"Require artifact provenance and integrity verification for production releases where supported.",
"Use reproducible or repeatable build practices when proportionate and technically feasible.",
"Maintain an inventory of source repositories, release branches and maintainers.",
"Define change approval, emergency change and rollback processes for security-sensitive releases.",
"Perform independent penetration testing for high-risk releases and major architecture changes.",
"Track test coverage by requirements and risk instead of using line coverage as a security-quality proxy.",
"Measure vulnerability age, recurrence, remediation SLA and exception expiry.",
]),
("SUPPLY","Software supply chain, dependencies and artifacts","external_tool","P1","core",["OWASP_TOP10","OWASP_ASVS","NIST_SSDF","CIS_CONTROLS","CYCLONEDX","SPDX","SLSA","OPENSSF_SCORECARD","CWE_TOP25"],[
"Maintain a resolved dependency inventory including transitive dependencies for each release artifact.",
"Generate a valid SBOM in an agreed format such as CycloneDX or SPDX from the resolved build output.",
"Scan direct and transitive dependencies for known vulnerabilities and record database freshness.",
"Map vulnerable components to exact package versions and deployed artifacts before assigning exposure.",
"Prioritize known-exploited CVEs using verified CISA KEV matches and contextual risk.",
"Use EPSS only as an exploit-likelihood input for known CVEs and preserve source timestamp.",
"Pin dependencies and review updates to reduce unreviewed drift and dependency confusion.",
"Verify package provenance/signatures where ecosystems provide reliable mechanisms.",
"Use private registry namespace controls and prevent dependency confusion.",
"Review package maintainership, update activity and unexpected install/build scripts for high-risk components.",
"Remove unused and abandoned dependencies from release artifacts.",
"Produce provenance linking source revision, workflow, builder, dependencies and output artifact.",
"Protect release signing keys and separate signing permissions from ordinary CI jobs.",
"Prevent secrets, test fixtures and local databases from entering source packages and release archives.",
"Scan container images and generated artifacts, not only source manifests.",
"Track license obligations and component attribution in accordance with organizational policy.",
"Define a vulnerability response policy for dependency advisories and upstream maintainer disclosures.",
"Record dependency scanner/tool version, database timestamp and triage decision for each release.",
]),
("CLOUD","Cloud, container, Kubernetes and infrastructure as code","manual_or_specialist_tool","P1","conditional",["OWASP_CLOUD_NATIVE","NIST_800_53","NIST_CSF","ISO27017","CIS_CONTROLS","CIS_BENCHMARKS","SLSA"],[
"Define shared-responsibility boundaries for each cloud service, managed platform and third-party provider.",
"Restrict cloud IAM roles, service accounts and workload identities to required actions/resources.",
"Prevent public access to storage, databases, snapshots and administrative services unless explicitly justified.",
"Store secrets in a managed secret service and avoid baking them into images or IaC state.",
"Scan IaC for public exposure, overly broad IAM, weak encryption and unsafe network rules.",
"Build containers from maintained minimal base images and rebuild when critical updates apply.",
"Run containers as non-root where feasible and remove unnecessary capabilities.",
"Use read-only filesystems, resource limits and seccomp/AppArmor or platform-equivalent controls where appropriate.",
"Pin container images by immutable digest for production deployments where feasible.",
"Restrict Kubernetes API access, RBAC, admission policy and exposed dashboards.",
"Avoid privileged pods, host-path mounts and broad host namespace access unless explicitly approved.",
"Separate workloads and secrets across environments and trust zones.",
"Apply egress controls for workloads that can fetch arbitrary URLs or contact external services.",
"Review cloud audit logging, key management, backup protection and configuration drift.",
"Use the exact CIS Benchmark release for the product and version being assessed.",
"Protect Terraform/CloudFormation state and CI plan output from secrets disclosure.",
"Require review and approval for infrastructure changes affecting internet exposure or access boundaries.",
"Test restore and failover for critical cloud resources and managed data services.",
]),
("AVAIL","Availability, resilience, rate limiting and recovery","manual_review","P1","core",["OWASP_API","OWASP_ATWA","NIST_CSF","NIST_800_53","ISO27001","ISO31000","NIST_800_61"],[
"Set explicit request, body, upload, response and processing timeouts throughout the stack.",
"Limit concurrency, queue length and per-tenant work to prevent resource starvation.",
"Apply rate limiting consistently across login, search, exports, API and expensive business paths.",
"Bound regular-expression, decompression, image/document and GraphQL query processing costs.",
"Define service-level objectives, availability targets and business impact of downtime.",
"Maintain tested backups with access separation, retention and recovery objectives.",
"Exercise restore and disaster-recovery procedures and record achieved recovery time/data loss.",
"Test safe degradation when identity, payment, messaging, database or third-party services are unavailable.",
"Use circuit breakers/retry budgets and avoid unbounded retries across dependencies.",
"Protect queues and scheduled work against unbounded growth, poison messages and repeated execution.",
"Assess availability risks from slow client reads, large responses and connection exhaustion.",
"Perform load/stress/DoS tests only with explicit authorization and an agreed safe environment/window.",
"Define operational thresholds and automatic stop rules for scans that increase target errors or latency.",
"Maintain rollback plans for deployment failures and security hotfixes.",
"Review multi-region/zone recovery and dependency single points of failure when the service needs them.",
]),
("VULN","Vulnerability management, disclosure and remediation","manual_review","P1","core",["ISO29147","ISO30111","NIST_800_61","NIST_CSF","OWASP_SAMM","OWASP_ASVS","CWE_TOP25","CVSS","EPSS","CISA_KEV"],[
"Maintain a published vulnerability reporting channel and a clear product security contact.",
"Define intake, acknowledgment, triage, reproduction, assignment, disclosure and closure workflows.",
"Assign unique finding IDs and preserve source scan, affected asset, evidence and remediation history.",
"Use CVSS v4.0 only when metrics and vector are defensibly assessed; keep heuristic risk separate.",
"Track confidence separately from impact/severity and require human verification for high-impact candidates.",
"Check KEV and EPSS data freshness when prioritizing known CVEs; record match rationale.",
"Set remediation SLAs by severity, exposure, exploitability and business context.",
"Require regression tests and retesting after fixes, with state transitions recorded.",
"Provide a documented false-positive process with rationale, reviewer and expiry/review date.",
"Require formal risk acceptance with compensating controls and an expiration date.",
"Coordinate disclosure with affected customers, maintainers and downstream users as appropriate.",
"Preserve sanitized evidence without collecting more sensitive data than necessary.",
"Track repeated/root-cause vulnerabilities and update design guidance or shared libraries.",
"Define a process for emergency mitigations when complete remediation is not immediately possible.",
"Provide customers with actionable advisories and upgrade/remediation guidance when disclosure is appropriate.",
]),
("PRIVREG","Privacy, legal and sectoral applicability review","interview_or_evidence","P1","conditional",["GDPR","NIS2","DORA","PCI_DSS","HIPAA","SOC2","ISO27701","NIST_PRIVACY","NIST_800_53"],[
"Record which jurisdictions, sectors, contracts and data types make regulatory checklists applicable.",
"Document controller/processor roles and data-processing terms where GDPR or equivalent privacy law applies.",
"Assess whether a data protection impact assessment is required for the processing context.",
"Map personal-data incident workflows to notification duties and applicable timelines through legal review.",
"For PCI DSS scope, document cardholder-data flows, connected systems and segmentation evidence.",
"For PCI DSS engagements, use required approved scanning/testing methods and qualified assessors where applicable.",
"For HIPAA scope, maintain risk analysis, access controls, audit controls and contingency evidence for ePHI.",
"For SOC 2, map controls to the applicable current AICPA Trust Services Criteria with the auditor.",
"For NIS2/DORA scope, verify entity classification, national law, sector rules and reporting obligations with counsel.",
"For cloud contracts, document shared responsibilities, subprocessors, regions and audit/evidence rights.",
"Do not claim GDPR, PCI, SOC 2, HIPAA, NIS2, DORA or ISO certification from scanner results alone.",
"Keep legal interpretations, applicability determinations and compliance sign-off owned by qualified personnel.",
]),
("ACCESS","Accessibility and inclusive product interface","automated_plus_manual","P2","adjacent",["WCAG22","EN301549","NIST_CSF"],[
"Provide keyboard access to all interactive controls without keyboard traps.",
"Maintain visible focus indicators and logical focus order.",
"Associate form labels, descriptions and error messages programmatically with controls.",
"Provide sufficient text and non-text contrast under the target WCAG conformance level.",
"Expose dynamic scan state, validation errors and status messages to assistive technologies.",
"Avoid relying on color alone to convey severity, status or error state.",
"Support zoom/reflow and responsive layouts without loss of critical functionality.",
"Provide meaningful accessible names for icon-only controls and report download actions.",
"Check focus movement and modal/dialog behavior in keyboard and screen-reader tests.",
"Include automated accessibility checks plus manual assistive-technology verification for applicable criteria.",
"Record target conformance level and applicable legal/procurement standard before declaring accessibility status.",
"Test language metadata, page title, headings and table header associations.",
]),
("MOBILE","Mobile application security (conditional)","specialist_tool","P2","conditional",["OWASP_MASVS","OWASP_MASTG","OWASP_ASVS","OWASP_CHEATSHEETS"],[
"Inventory mobile app identifiers, signing keys, supported platform versions and release channels.",
"Avoid storing long-lived secrets or sensitive records in insecure device storage.",
"Use platform-backed key storage and modern cryptographic APIs for sensitive mobile data.",
"Validate TLS and certificate behavior, including unsafe trust overrides and debug-only network settings.",
"Protect deep links, app links, intent handlers and inter-app messages against unauthorized actions.",
"Review exported Android components, entitlements, URL schemes and platform permissions.",
"Prevent sensitive data from leaking through logs, screenshots, clipboard, backups or notifications where relevant.",
"Review root/jailbreak, tampering and reverse-engineering mitigations according to actual risk.",
"Use MASVS and MASTG test cases for each supported platform and record device/OS/tool versions.",
"Treat a web/API scan as complementary; do not claim mobile MASVS conformance without mobile testing.",
]),
("AI","AI/LLM/agent security (conditional)","manual_or_specialist_tool","P1","conditional",["OWASP_LLM","NIST_AI_RMF","NIST_AI_GENAI","ISO42001","NIST_PRIVACY"],[
"Inventory models, model versions, providers, prompts, tools, retrieval sources and sensitive data paths.",
"Test direct and indirect prompt-injection resistance using approved, non-destructive test fixtures.",
"Prevent untrusted retrieved content from gaining system-level authority or bypassing policy constraints.",
"Apply least privilege and per-tool authorization to agent actions; require approval for high-impact actions.",
"Validate and constrain model outputs before SQL, shell, HTML, code, URL or API execution.",
"Limit token use, tool calls, recursion, response size and external-call spend to prevent resource abuse.",
"Prevent model prompts, hidden system instructions, credentials and private retrieval context from being disclosed.",
"Isolate tenants and enforce authorization at retrieval time, not only in prompt instructions.",
"Validate data provenance and access controls for embeddings, vector stores, training and fine-tuning data.",
"Evaluate model supply-chain risk, plugins/tools, external data and model licensing/provenance.",
"Log model/tool actions with redaction and reconstructable trace IDs without retaining unnecessary private content.",
"Perform human review and incident handling for high-impact AI outputs and automated decisions.",
"Document known limitations, evaluation datasets, misuse tests, acceptance thresholds and rollback criteria.",
"Do not treat generic prompt safety filters as proof that prompt injection or data exfiltration is impossible.",
]),
("SCANNER","Security testing product / scanner assurance","manual_or_evidence","P0","core",["OWASP_ASVS","OWASP_WSTG","NIST_800_115","NIST_SSDF","ISO27034","ISO27001","ISO30111","CVSS","SARIF"],[
"Require a fail-closed target scope check before every network request and follow-up operation.",
"Revalidate scope after redirects, DNS resolution changes and browser-generated requests.",
"Never forward credentials across scheme/host/port origins without an explicit separate credential profile.",
"Enforce per-job rate, concurrency, page, depth, endpoint, byte and time budgets.",
"Provide cancellation checkpoints and ensure canceled scans stop issuing new requests promptly.",
"Redact tokens, passwords, session IDs and secret-like data before database/log/report persistence.",
"Do not execute arbitrary shell commands or code generated by an LLM or remote target content.",
"Treat target HTML, JS, headers and API specifications as untrusted input and prevent prompt/code injection into tooling.",
"Keep optional ZAP or specialist-tool adapters disabled by default and scope their URLs independently.",
"Use a dedicated isolated test target for E2E tests; do not point automated tests at public targets.",
"Test HTTP client behavior for redirect, DNS/IP policy, TLS errors, decompression limits and malformed responses.",
"Store scan configuration and result provenance without storing raw credentials.",
"Ensure report bundles contain only files for that scan and verify path/size/hash consistency.",
"Use a stable documented finding schema with rule IDs, confidence, severity, evidence, remediation and references.",
"Distinguish no finding, not tested, not applicable, blocked and manually required states.",
"Track scanner version, rule-set version, dependency inventory and start/end timestamps in each report.",
"Run static analysis, dependency audit, secret scanning and container scanning in release CI.",
"Document the scanner’s false-positive/false-negative limitations and do not claim complete vulnerability detection.",
"Require independent review of new rules that can produce outbound requests or inspect sensitive content.",
"Ensure dashboard output escapes target-derived data and uses safe DOM rendering practices.",
]),
("EVIDENCE","Evidence integrity, reporting and audit trail","manual_or_evidence","P1","core",["OWASP_WSTG","NIST_800_115","NIST_800_53","ISO27001","SARIF","CVSS","ISO29147","ISO30111"],[
"Every finding identifies the test/rule version, target asset, observation time and verification mode.",
"Store minimum necessary sanitized evidence and redact secrets before persistence.",
"Distinguish observed fact, hypothesis, inference and manually verified conclusion in reports.",
"Include expected behavior, observed behavior, impact, remediation and retest guidance.",
"Include coverage and untested limitations in every assessment summary.",
"Provide JSON schema/versioning and validate emitted report formats in CI.",
"Escape HTML/Markdown and neutralize CSV formula injection in export paths.",
"Validate SARIF output with schema and preserve correct rule metadata and result locations.",
"Include SHA-256 manifest entries for report bundles and clearly label unsigned manifests.",
"Protect reports using access control, transport security, retention limits and auditable download events.",
"Maintain an audit trail for finding state changes and standards-checklist decisions.",
"Require reviewer/approver details and rationale for high-severity closure or risk acceptance.",
]),
("STANDARDS","Standards mapping and conformity governance","manual_or_evidence","P1","core",["OWASP_ASVS","OWASP_WSTG","OWASP_TOP10","OWASP_API","NIST_CSF","ISO27001","ISO27002","ISO31000"],[
"Record each framework version and the official source URL used for the assessment baseline.",
"Keep direct standards, guidance, legal obligations and adjacent references explicitly distinguished.",
"Use stable local checklist IDs and preserve official clause identifiers only where independently verified.",
"Map each checklist item to one or more framework families with a documented mapping rationale.",
"Record applicability decision, scope rationale and approver for every conditional control.",
"Maintain status states for not assessed, compliant, partially compliant, non-compliant, not applicable, blocked and evidence pending.",
"Require evidence and reviewer identity before a control can be marked compliant.",
"Require written justification and approval before a control can be marked not applicable.",
"Reassess versioned standards when an official edition changes or is superseded.",
"Make clear that a curated crosswalk is not a complete clause-by-clause transcription or certification.",
"Track standard-to-control mapping gaps and distinguish unmapped controls from controls not tested.",
"Export a dated checklist with filters, owner, status, evidence and change history for audit review.",
]),
("RELEASE","Release, operations, backup and product governance","interview_or_evidence","P1","core",["NIST_SSDF","NIST_CSF","NIST_800_53","ISO27001","ISO27035","CIS_CONTROLS","SLSA","OPENSSF_SCORECARD","CISA_SECURE_BY_DESIGN"],[
"Run all required unit, contract, integration and local E2E tests before a release is tagged.",
"Apply a reproducible test inventory, coverage threshold and release decision record.",
"Test database migration/upgrade behavior and document rollback procedures.",
"Verify Docker image build, runtime non-root posture, health checks and minimal published ports.",
"Generate resolved SBOM and image scan results for distributable release artifacts.",
"Sign release artifacts or publish verifiable provenance where infrastructure supports it.",
"Publish release notes, known limitations, support policy and security reporting contact.",
"Protect default branch with reviews and required CI for production repositories.",
"Use minimum permissions and pinned third-party actions in CI/CD workflows.",
"Monitor dependency and base-image vulnerabilities and define update SLAs.",
"Test recovery of application database, checklist state and report evidence backups.",
"Define product support/end-of-life policy and security update cadence.",
"Record release approver, source commit, build workflow, artifact hashes and deployment environment.",
"Perform rollback or hotfix drills for critical security defects.",
]),
("ACCESSIBILITY_REG","Accessibility conformance governance","manual_review","P2","conditional",["WCAG22","EN301549","ISO27001"],[
"Define required WCAG conformance level and applicable national/procurement accessibility obligations.",
"Document automated accessibility tool scope and the criteria that require manual assessment.",
"Perform manual keyboard, focus, screen-reader and cognitive/interaction review for critical workflows.",
"Record exceptions, remediation owners and dates for accessibility defects.",
]),
("IDENTITY_PROTOCOLS","Identity protocol configuration and token lifecycle","manual_review","P1","conditional",["NIST_800_63","OAUTH_RFC9700","JWT_RFC8725","OIDC","PKCE_RFC7636","OWASP_ASVS"],[
"Publish and validate authorization-server metadata where supported.",
"Validate ID token issuer, audience, nonce, signature, expiry and token type in OIDC clients.",
"Reject OAuth redirect URIs that are not exact registered matches, except protocol-defined native loopback cases.",
"Use modern OAuth flows and reject deprecated/insecure grants or response patterns where applicable.",
"Scope access tokens narrowly and enforce audience/resource-server validation.",
"Define token revocation, rotation and incident handling for stolen credentials.",
]),
("HTTP_PROTOCOLS","Protocol correctness and edge cases","automated_readonly","P2","core",["HTTP_RFC9110","OWASP_WSTG","OWASP_ASVS"],[
"Handle HTTP methods and status codes consistently with the intended resource semantics.",
"Reject malformed request framing and ambiguous content-length/transfer-encoding combinations at trusted gateways.",
"Normalize header names case-insensitively without allowing duplicate security-sensitive fields to bypass policy.",
"Avoid request smuggling-prone disagreement between reverse proxies and application servers.",
"Apply body/header size and timeout limits consistently across proxies and origin services.",
"Do not expose TRACE or unexpected administrative methods without a documented requirement.",
]),
("SUPPORT","Security support, customer communication and disclosure","manual_review","P2","core",["ISO29147","ISO30111","NIST_800_61","CISA_SECURE_BY_DESIGN"],[
"Publish security contact metadata such as security.txt according to the chosen policy and RFC guidance.",
"Provide a clear intake process for researchers with acknowledgment and safe-harbor terms where appropriate.",
"Define coordinated disclosure timelines, customer notification criteria and embargo handling.",
"Ensure advisories identify affected versions, severity rationale, mitigation and fixed versions.",
"Track external vulnerability reports through closure and feed lessons learned into product tests.",
]),
]

# Verify malformed domains and framework IDs before generating deliverables.
for row in DOMAINS:
    if not isinstance(row[5], list):
        raise ValueError(f"Framework mapping must be list in domain {row[0]}")

FRAMEWORK_BY_ID = {f[0]: f for f in FRAMEWORKS}
controls = []
for code, domain, default_mode, default_priority, applicability, framework_ids, items in DOMAINS:
    for idx, item in enumerate(items, 1):
        cid = f"FWPRO-{code}-{idx:03d}"
        low = item.lower()
        mode = default_mode
        if any(k in low for k in ["scan", "discover", "parse", "record http", "headers", "redirect", "tls", "cookie", "cors", "manifest", "hash", "csv", "html", "json schema"]):
            if default_mode in {"automated_passive", "automated_readonly", "automated_plus_manual"}:
                mode = default_mode
        if any(k in low for k in ["test ", "verify ", "check ", "validate ", "detect ", "reject ", "ensure ", "prevent ", "disable ", "limit ", "apply ", "use ", "set "]):
            if default_mode == "manual_review" and code in {"GOV","RISK","ARCH","AUTHN","AUTHZ","DATA","BUSINESS","ERROR","VULN","PRIVREG","SUPPORT"}:
                mode = default_mode
        if code in {"MOBILE","AI","CLOUD","SUPPLY","FILES"}:
            mode = default_mode
        # Extend mappings conservatively with cross-cutting standards based on domain.
        maps = list(framework_ids)
        if code in {"INPUT","API","HTTP_PROTOCOLS"}:
            for x in ["OWASP_TOP10","OWASP_API","CWE_TOP25"]:
                if x not in maps: maps.append(x)
        if code in {"AUTHN","AUTHZ","SESSION","IDENTITY_PROTOCOLS"}:
            for x in ["OWASP_ASVS","NIST_800_63","NIST_800_53"]:
                if x not in maps: maps.append(x)
        if code in {"SUPPLY","SDLC","RELEASE"}:
            for x in ["NIST_SSDF","OPENSSF_SCORECARD","SLSA","SLSA_PROVENANCE"]:
                if x in FRAMEWORK_BY_ID and x not in maps: maps.append(x)
        if code in {"DATA","PRIVREG"} and "NIST_PRIVACY" not in maps: maps.append("NIST_PRIVACY")
        if code in {"AI"}:
            for x in ["OWASP_LLM","NIST_AI_RMF","NIST_AI_GENAI","ISO42001"]:
                if x not in maps: maps.append(x)
        # Per-control metadata stays editable in the workbook/API.
        evidence_examples = {
            "automated_passive": "Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.",
            "automated_readonly": "Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.",
            "automated_plus_manual": "Automated scan result plus manual keyboard/screen-reader verification evidence.",
            "manual_review": "Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.",
            "manual_or_specialist_tool": "Reproducible test case, approved test account/environment, tool/version and reviewer validation.",
            "interview_or_evidence": "Approved policy/process, responsible owner, sample records, review cadence and exceptions log.",
            "external_tool": "Tool name/version, database freshness, machine-readable output and triage record.",
            "specialist_tool": "Specialist tool/test record, device/environment details, sanitized evidence and assessor review.",
        }
        owner = {
            "GOV":"Security Lead / Engagement Owner", "RISK":"Security Architect / Risk Owner", "ASSET":"AppSec / Asset Owner", "ARCH":"Security Architect",
            "AUTHN":"Identity Engineer / AppSec", "AUTHZ":"App Owner / AppSec", "SESSION":"Web Engineer / AppSec", "INPUT":"AppSec / Engineering",
            "API":"API Owner / AppSec", "WEB":"Platform / Web Engineering", "CRYPTO":"Platform Security / Key Owner", "DATA":"Privacy / Data Owner",
            "FILES":"Backend Owner / AppSec", "BUSINESS":"Product Owner / AppSec", "ERROR":"SRE / SOC / Security Operations", "SDLC":"Engineering Leadership / AppSec",
            "SUPPLY":"Platform / Supply-chain Security", "CLOUD":"Cloud Security / Platform", "AVAIL":"SRE / Service Owner", "VULN":"Product Security / PSIRT",
            "PRIVREG":"Privacy / Legal / Compliance", "ACCESS":"UX / Accessibility Lead", "MOBILE":"Mobile Lead / Mobile AppSec", "AI":"AI Platform / AI Security",
            "SCANNER":"FIREWATCH Maintainer / Product Security", "EVIDENCE":"Assessment Lead / Auditor", "STANDARDS":"Compliance Owner / AppSec",
            "RELEASE":"Release Manager / Platform", "ACCESSIBILITY_REG":"Accessibility Owner", "IDENTITY_PROTOCOLS":"Identity Architect", "HTTP_PROTOCOLS":"Platform / Gateway Owner", "SUPPORT":"PSIRT / Customer Security",
        }.get(code, "Control Owner")
        # Tailor acceptance statement to avoid implying a simple checkbox is adequate.
        if mode in {"automated_passive", "automated_readonly"}:
            acceptance = f"A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: {item}"
        elif mode in {"interview_or_evidence", "manual_review"}:
            acceptance = f"An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: {item}"
        else:
            acceptance = f"Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: {item}"
        controls.append({
            "id": cid, "domain_id": code, "domain": domain, "requirement": item,
            "acceptance_criteria": acceptance, "expected_evidence": evidence_examples.get(mode, evidence_examples["manual_review"]),
            "verification_mode": mode, "priority": default_priority, "applicability": applicability,
            "framework_ids": maps,
            "relationship_types": sorted({FRAMEWORK_BY_ID[fid][3] for fid in maps if fid in FRAMEWORK_BY_ID}),
            "relationship": "; ".join(sorted({FRAMEWORK_BY_ID[fid][3] for fid in maps if fid in FRAMEWORK_BY_ID})),
            "framework_mappings": [
                {"framework_id": fid, "framework_name": FRAMEWORK_BY_ID[fid][1], "version": FRAMEWORK_BY_ID[fid][2],
                 "mapping_note": f"Related subject/family mapping only; validate exact official clauses/requirements against the cited edition before claiming conformance."}
                for fid in maps if fid in FRAMEWORK_BY_ID
            ],
            "owner_role": owner, "status": "not_assessed", "owner": "", "due_date": "", "evidence_url": "", "evidence_note": "",
            "reviewer": "", "last_reviewed": "", "justification": "", "source_urls": [FRAMEWORK_BY_ID[fid][5] for fid in maps if fid in FRAMEWORK_BY_ID],
            "status_options": ["not_assessed","compliant","partially_compliant","non_compliant","not_applicable","blocked","evidence_pending"],
            "automation_note": "Checklist item; the FIREWATCH web scanner automates only the subset explicitly represented by active rules. Non-automated controls require evidence/reviewer workflow.",
        })

# Build mapping index and stats.
framework_counts = Counter(fid for c in controls for fid in c["framework_ids"])
domain_counts = Counter(c["domain_id"] for c in controls)
registry = []
for f in FRAMEWORKS:
    fid, title, version, relation, applicability_f, url, caveat = f
    registry.append({"id": fid, "name": title, "version_or_status": version, "relationship": relation,
                     "applicability": applicability_f, "official_url": url, "use_and_limitations": caveat,
                     "mapped_control_count": framework_counts.get(fid, 0), "last_verified": AS_OF})

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "standards_registry.json").write_text(json.dumps({"edition":"FIREWATCH Sentinel v9", "as_of":AS_OF, "framework_count":len(registry), "frameworks":registry}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
(OUT / "standards_checklist.json").write_text(json.dumps({"edition":"FIREWATCH Sentinel v9", "schema_version":"1.0", "as_of":AS_OF, "total_controls":len(controls), "domain_count":len(DOMAINS), "framework_count":len(registry), "status_options":["not_assessed","compliant","partially_compliant","non_compliant","not_applicable","blocked","evidence_pending"], "important_notice":"Curated original crosswalk; not a clause-complete copy of every referenced publication, certification or legal opinion. Assess applicability with competent owners and consult the official source texts.", "controls":controls}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

csv_fields = ["id","domain_id","domain","requirement","acceptance_criteria","expected_evidence","verification_mode","priority","applicability","relationship","relationship_types","framework_ids","framework_names","owner_role","status","owner","due_date","evidence_url","evidence_note","reviewer","last_reviewed","justification","source_urls"]
with (OUT / "standards_checklist.csv").open("w", newline="", encoding="utf-8-sig") as fp:
    writer = csv.DictWriter(fp, fieldnames=csv_fields, extrasaction="ignore")
    writer.writeheader()
    for c in controls:
        row = dict(c)
        row["framework_ids"] = ";".join(c["framework_ids"])
        row["framework_names"] = ";".join(m["framework_name"] for m in c["framework_mappings"])
        row["source_urls"] = ";".join(c["source_urls"])
        writer.writerow(row)

with (OUT / "framework_register.csv").open("w", newline="", encoding="utf-8-sig") as fp:
    fields = ["id","name","version_or_status","relationship","applicability","official_url","use_and_limitations","mapped_control_count","last_verified"]
    writer = csv.DictWriter(fp, fieldnames=fields)
    writer.writeheader()
    writer.writerows(registry)

# Markdown handbook with registry and compact control list; Excel is generated separately.
rel_labels = {"direct":"مستقیم/هسته‌ای", "supporting":"پشتیبان/حاکمیتی", "conditional":"مشروط به دامنه", "adjacent":"مجاور/تکمیلی"}
lines = [
"# FIREWATCH Sentinel v9 — Standards & Compliance Readiness Checklist",
"", f"**تاریخ بررسی منابع:** {AS_OF}  ", f"**چارچوب‌ها/استانداردهای مرجع:** {len(registry)}  | **کنترل‌های چک‌لیست:** {len(controls)}  | **حوزه‌ها:** {len(DOMAINS)}",
"", "> **حدود ادعا:** این یک crosswalk عملیاتی و بازنویسی‌شده است؛ بازتولید کامل متن استانداردها نیست و به‌تنهایی اثبات انطباق، certification یا نظر حقوقی محسوب نمی‌شود. تطبیق بندبه‌بند باید با متن رسمی و نسخه‌ی قراردادی/قانونی جاری انجام شود. «یافته‌ای ثبت نشد» برابر با «کنترل منطبق است» نیست.",
"", "## نحوه‌ی استفاده",
"1. ابتدا Scope و applicability هر framework را با مالک فنی/حقوقی تأیید کنید.",
"2. هر control را فقط پس از بررسی شواهد جاری به `compliant` تغییر دهید؛ نتیجه‌ی خودکار به تنهایی برای controls دستی کافی نیست.",
"3. `not_applicable` نیازمند توجیه و تأیید است؛ `blocked` و `evidence_pending` را از وضعیت پاس جدا نگه دارید.",
"4. برای هر finding، شواهد sanitized، تاریخ، ابزار/نسخه، reviewer و remediation ثبت شود.",
"5. از Workbook برای مدیریت وضعیت‌ها استفاده کنید یا از API محافظت‌شده‌ی `/api/v1/standards/*` و تاریخچه‌ی تغییرات بهره ببرید.",
"6. برای هر framework فقط subset مرتبط را انتخاب کنید؛ چارچوب‌های قانونی/صنعتی همیشه نیازمند ارزیابی applicability هستند.",
"", "## واژگان رابطه و قابلیت اجرا",
"- **direct:** مستقیماً به تست وب/API و کنترل‌های فنی مرتبط است.",
"- **supporting:** به SDLC، عملیات، گزارش‌دهی، ریسک و مدیریت امنیت محصول کمک می‌کند.",
"- **conditional:** فقط در صورت وجود فناوری/صنعت/قانون/مدل عملیاتی مربوط اعمال می‌شود.",
"- **adjacent:** موضوع مرتبط ولی غیرامنیتی یا فرعی (مثل دسترس‌پذیری) که برای محصول صنعتی ممکن است مهم باشد.",
"- `automated_passive` / `automated_readonly`: مناسب مشاهده/درخواست کم‌خطر؛ فقط در حد ruleهای پیاده‌سازی‌شده.",
"- `manual_review` / `interview_or_evidence`: نیازمند reviewer، سند یا آزمون دستی.",
"- `external_tool` / `specialist_tool`: نیازمند ابزار یا محیط تخصصی.",
"", "## فهرست frameworkها و استانداردهای مرجع", "", "| ID | مرجع | نسخه/وضعیت | رابطه | تعداد کنترل‌های mapped | منبع رسمی |", "|---|---|---|---|---:|---|"]
for f in registry:
    lines.append(f"| {f['id']} | {f['name']} | {f['version_or_status']} | {rel_labels.get(f['relationship'], f['relationship'])} | {f['mapped_control_count']} | [Official]({f['official_url']}) |")
lines += ["", "## خلاصه‌ی کنترل‌ها بر اساس حوزه", "", "| شناسه حوزه | حوزه | تعداد |", "|---|---|---:|"]
for d in DOMAINS:
    lines.append(f"| {d[0]} | {d[1]} | {domain_counts[d[0]]} |")
lines += ["", "## چک‌لیست کامل و جزئی کنترل‌ها", "", "هر کنترل شامل هدف، معیار پذیرش، شواهد مورد انتظار، روش راستی‌آزمایی، اولویت، سطح applicability، رابطه با مراجع و URLهای رسمی است. متن کنترل‌ها بازنویسی مستقل است و نباید به‌عنوان نقل‌قول بند استاندارد تلقی شود."]
for domain_row in DOMAINS:
    domain_code, domain_name = domain_row[0], domain_row[1]
    domain_controls = [c for c in controls if c["domain_id"] == domain_code]
    lines += ["", f"### {domain_code} — {domain_name} ({len(domain_controls)} کنترل)"]
    for c in domain_controls:
        framework_text = "; ".join(c["framework_ids"])
        source_links = " · ".join(f"[{fid}]({FRAMEWORK_BY_ID[fid][5]})" for fid in c["framework_ids"] if fid in FRAMEWORK_BY_ID)
        lines += [
            "", f"#### `{c['id']}` — {c['priority']} / {c['applicability']}",
            f"- **هدف کنترل:** {c['requirement']}",
            f"- **معیار پذیرش:** {c['acceptance_criteria']}",
            f"- **شواهد مورد انتظار:** {c['expected_evidence']}",
            f"- **روش راستی‌آزمایی:** `{c['verification_mode']}`",
            f"- **نوع رابطه با مراجع:** {', '.join(c['relationship_types'])}",
            f"- **مراجع مرتبط:** `{framework_text}`",
            f"- **منابع رسمی:** {source_links}",
        ]
lines += ["", "## نکته‌ی نسخه و حق نشر", "", "نسخه‌های مرجع در تاریخ بالا از صفحات رسمی بررسی شده‌اند؛ استانداردهای rolling/under-review ممکن است تغییر کنند. عناوین و URLها برای ارجاع هستند؛ متن‌های کنترل این فایل بازنویسی و خلاصه‌ی مستقل هستند و جایگزین متن کامل استانداردهای دارای حق نشر یا مستندات رسمی نیستند."]
(OUT / "STANDARDS_CHECKLIST.md").write_text("\n".join(lines)+"\n", encoding="utf-8")

# Machine-readable test/quality summary.
summary = {
    "edition":"FIREWATCH Sentinel v9", "generated_at":AS_OF,
    "framework_count":len(registry), "domain_count":len(DOMAINS), "control_count":len(controls),
    "controls_by_domain":dict(domain_counts),
    "controls_by_priority":dict(Counter(c["priority"] for c in controls)),
    "controls_by_verification_mode":dict(Counter(c["verification_mode"] for c in controls)),
    "controls_by_applicability":dict(Counter(c["applicability"] for c in controls)),
    "controls_by_relationship":dict(Counter(rel for c in controls for rel in [FRAMEWORK_BY_ID[fid][3] for fid in c["framework_ids"]])),
    "claims": "The count is the number of curated checklist records, not the number of official clauses or tests actually executed."
}
(OUT / "standards_checklist_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"frameworks":len(registry),"domains":len(DOMAINS),"controls":len(controls),"mode_counts":summary["controls_by_verification_mode"]}, indent=2))
