# FIREWATCH Sentinel v9 — Standards & Compliance Readiness Checklist

**تاریخ بررسی منابع:** 2026-10-15  
**چارچوب‌ها/استانداردهای مرجع:** 67  | **کنترل‌های چک‌لیست:** 469  | **حوزه‌ها:** 32

> **حدود ادعا:** این یک crosswalk عملیاتی و بازنویسی‌شده است؛ بازتولید کامل متن استانداردها نیست و به‌تنهایی اثبات انطباق، certification یا نظر حقوقی محسوب نمی‌شود. تطبیق بندبه‌بند باید با متن رسمی و نسخه‌ی قراردادی/قانونی جاری انجام شود. «یافته‌ای ثبت نشد» برابر با «کنترل منطبق است» نیست.

## نحوه‌ی استفاده
1. ابتدا Scope و applicability هر framework را با مالک فنی/حقوقی تأیید کنید.
2. هر control را فقط پس از بررسی شواهد جاری به `compliant` تغییر دهید؛ نتیجه‌ی خودکار به تنهایی برای controls دستی کافی نیست.
3. `not_applicable` نیازمند توجیه و تأیید است؛ `blocked` و `evidence_pending` را از وضعیت پاس جدا نگه دارید.
4. برای هر finding، شواهد sanitized، تاریخ، ابزار/نسخه، reviewer و remediation ثبت شود.
5. از Workbook برای مدیریت وضعیت‌ها استفاده کنید یا از API محافظت‌شده‌ی `/api/v1/standards/*` و تاریخچه‌ی تغییرات بهره ببرید.
6. برای هر framework فقط subset مرتبط را انتخاب کنید؛ چارچوب‌های قانونی/صنعتی همیشه نیازمند ارزیابی applicability هستند.

## واژگان رابطه و قابلیت اجرا
- **direct:** مستقیماً به تست وب/API و کنترل‌های فنی مرتبط است.
- **supporting:** به SDLC، عملیات، گزارش‌دهی، ریسک و مدیریت امنیت محصول کمک می‌کند.
- **conditional:** فقط در صورت وجود فناوری/صنعت/قانون/مدل عملیاتی مربوط اعمال می‌شود.
- **adjacent:** موضوع مرتبط ولی غیرامنیتی یا فرعی (مثل دسترس‌پذیری) که برای محصول صنعتی ممکن است مهم باشد.
- `automated_passive` / `automated_readonly`: مناسب مشاهده/درخواست کم‌خطر؛ فقط در حد ruleهای پیاده‌سازی‌شده.
- `manual_review` / `interview_or_evidence`: نیازمند reviewer، سند یا آزمون دستی.
- `external_tool` / `specialist_tool`: نیازمند ابزار یا محیط تخصصی.

## فهرست frameworkها و استانداردهای مرجع

| ID | مرجع | نسخه/وضعیت | رابطه | تعداد کنترل‌های mapped | منبع رسمی |
|---|---|---|---|---:|---|
| OWASP_ASVS | OWASP Application Security Verification Standard | 5.0.0 (stable) | مستقیم/هسته‌ای | 328 | [Official](https://owasp.org/www-project-application-security-verification-standard/) |
| OWASP_WSTG | OWASP Web Security Testing Guide | v4.2 (current stable) | مستقیم/هسته‌ای | 259 | [Official](https://owasp.org/www-project-web-security-testing-guide/v42/) |
| OWASP_TOP10 | OWASP Top 10 | 2025 (released) | مستقیم/هسته‌ای | 225 | [Official](https://owasp.org/projects/top-ten) |
| OWASP_API | OWASP API Security Top 10 | 2023 | مستقیم/هسته‌ای | 136 | [Official](https://owasp.org/www-project-api-security/) |
| OWASP_CHEATSHEETS | OWASP Cheat Sheet Series | Rolling community guidance | پشتیبان/حاکمیتی | 60 | [Official](https://cheatsheetseries.owasp.org/) |
| OWASP_SAMM | OWASP Software Assurance Maturity Model | 2.2.0 (project-listed) | پشتیبان/حاکمیتی | 66 | [Official](https://owaspsamm.org/model/) |
| OWASP_MASVS | OWASP Mobile Application Security Verification Standard | Current project edition; verify at assessment time | مشروط به دامنه | 10 | [Official](https://mas.owasp.org/MASVS/) |
| OWASP_MASTG | OWASP Mobile Application Security Testing Guide | Rolling project content | مشروط به دامنه | 10 | [Official](https://mas.owasp.org/MASTG/) |
| OWASP_LLM | OWASP Top 10 for LLM Applications | 2025 | مشروط به دامنه | 14 | [Official](https://genai.owasp.org/llm-top-10/) |
| OWASP_ATWA | OWASP Automated Threats to Web Applications | 2023 project edition / verify current project page | پشتیبان/حاکمیتی | 30 | [Official](https://owasp.org/www-project-automated-threats-to-web-applications/) |
| OWASP_CLOUD_NATIVE | OWASP Cloud-Native Application Security Top 10 | Project material marked interim/under review | مجاور/تکمیلی | 18 | [Official](https://owasp.org/projects/cloud-native-application-security-top-10) |
| NIST_800_115 | NIST SP 800-115 | 2008 (published guide; check errata/current context) | پشتیبان/حاکمیتی | 52 | [Official](https://csrc.nist.gov/pubs/sp/800/115/final) |
| NIST_SSDF | NIST SP 800-218 Secure Software Development Framework | 1.1 | پشتیبان/حاکمیتی | 87 | [Official](https://csrc.nist.gov/pubs/sp/800/218/final) |
| NIST_CSF | NIST Cybersecurity Framework | 2.0 | پشتیبان/حاکمیتی | 187 | [Official](https://www.nist.gov/cyberframework) |
| NIST_800_53 | NIST SP 800-53 Security and Privacy Controls | Rev. 5 + current errata | پشتیبان/حاکمیتی | 210 | [Official](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) |
| NIST_800_63 | NIST SP 800-63 Digital Identity Guidelines | Revision 4 (2025) | پشتیبان/حاکمیتی | 59 | [Official](https://csrc.nist.gov/pubs/sp/800/63/4/final) |
| NIST_PRIVACY | NIST Privacy Framework | 1.0 | پشتیبان/حاکمیتی | 42 | [Official](https://www.nist.gov/privacy-framework) |
| NIST_AI_RMF | NIST AI Risk Management Framework | 1.0 | مشروط به دامنه | 14 | [Official](https://www.nist.gov/itl/ai-risk-management-framework) |
| NIST_AI_GENAI | NIST AI RMF Generative AI Profile | 1.0 | مشروط به دامنه | 14 | [Official](https://www.nist.gov/itl/ai-risk-management-framework) |
| NIST_800_61 | NIST SP 800-61 Incident Response | Rev. 3 (2025) | پشتیبان/حاکمیتی | 50 | [Official](https://csrc.nist.gov/pubs/sp/800/61/r3/final) |
| ISO27001 | ISO/IEC 27001 | 2022 | پشتیبان/حاکمیتی | 148 | [Official](https://www.iso.org/standard/27001) |
| ISO27002 | ISO/IEC 27002 | 2022 | پشتیبان/حاکمیتی | 50 | [Official](https://www.iso.org/standard/75652.html) |
| ISO27034 | ISO/IEC 27034-1 Application Security | 2011; reviewed/confirmed current in 2022 | مستقیم/هسته‌ای | 55 | [Official](https://www.iso.org/standard/44378.html) |
| ISO27017 | ISO/IEC 27017 Cloud Security Controls | 2026 edition | مشروط به دامنه | 18 | [Official](https://www.iso.org/standard/27017) |
| ISO27701 | ISO/IEC 27701 Privacy Information Management | 2025 edition | مشروط به دامنه | 28 | [Official](https://www.iso.org/standard/27701) |
| ISO27035 | ISO/IEC 27035-1 Incident Management | 2023 | پشتیبان/حاکمیتی | 29 | [Official](https://www.iso.org/standard/78973.html) |
| ISO29147 | ISO/IEC 29147 Vulnerability Disclosure | 2018; reviewed/confirmed current in 2024 | پشتیبان/حاکمیتی | 32 | [Official](https://www.iso.org/standard/72311.html) |
| ISO30111 | ISO/IEC 30111 Vulnerability Handling | 2019; reviewed/confirmed current in 2025 | پشتیبان/حاکمیتی | 52 | [Official](https://www.iso.org/standard/69725.html) |
| ISO31000 | ISO 31000 Risk Management | 2018; reviewed/confirmed current in 2023 | پشتیبان/حاکمیتی | 78 | [Official](https://www.iso.org/standard/65694.html) |
| GDPR | EU General Data Protection Regulation | Regulation (EU) 2016/679, as applicable/current consolidated text | مشروط به دامنه | 28 | [Official](https://eur-lex.europa.eu/eli/reg/2016/679/oj) |
| NIS2 | EU NIS2 Directive | Directive (EU) 2022/2555; national transposition applies | مشروط به دامنه | 12 | [Official](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) |
| DORA | EU Digital Operational Resilience Act | Regulation (EU) 2022/2554 | مشروط به دامنه | 12 | [Official](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) |
| PCI_DSS | PCI DSS | v4.0.1 | مشروط به دامنه | 28 | [Official](https://www.pcisecuritystandards.org/document_library/) |
| HIPAA | HIPAA Security Rule | Current U.S. HHS rule and guidance | مشروط به دامنه | 28 | [Official](https://www.hhs.gov/hipaa/for-professionals/security/index.html) |
| SOC2 | AICPA Trust Services Criteria / SOC 2 | Current licensed criteria; verify with AICPA | مشروط به دامنه | 12 | [Official](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) |
| WCAG22 | W3C Web Content Accessibility Guidelines | 2.2 W3C Recommendation | مجاور/تکمیلی | 16 | [Official](https://www.w3.org/TR/WCAG22/) |
| EN301549 | ETSI EN 301 549 accessibility requirements for ICT | Use current applicable edition | مشروط به دامنه | 16 | [Official](https://www.etsi.org/standards) |
| OPENAPI | OpenAPI Specification | 3.2.1 current published line | مستقیم/هسته‌ای | 20 | [Official](https://spec.openapis.org/oas/) |
| JSON_SCHEMA | JSON Schema | 2020-12 family; verify dialect declared by API | پشتیبان/حاکمیتی | 20 | [Official](https://json-schema.org/specification) |
| HTTP_RFC9110 | IETF RFC 9110 HTTP Semantics | 2022, current with subsequent RFC updates | مستقیم/هسته‌ای | 44 | [Official](https://www.rfc-editor.org/rfc/rfc9110.html) |
| TLS_RFC8446 | IETF RFC 8446 TLS 1.3 | 2018, current specification with updates | مستقیم/هسته‌ای | 18 | [Official](https://www.rfc-editor.org/rfc/rfc8446.html) |
| TLS_BCP | IETF RFC 9325 and updates including RFC 9852 | RFC 9852 (July 2026) updates BCP 195 | مستقیم/هسته‌ای | 18 | [Official](https://www.rfc-editor.org/rfc/rfc9852.html) |
| HSTS_RFC6797 | IETF RFC 6797 HTTP Strict Transport Security | 2012; use with current browser behavior | مستقیم/هسته‌ای | 18 | [Official](https://www.rfc-editor.org/rfc/rfc6797.html) |
| OAUTH_RFC9700 | IETF RFC 9700 OAuth 2.0 Security BCP | 2025 | مشروط به دامنه | 26 | [Official](https://www.rfc-editor.org/rfc/rfc9700.html) |
| JWT_RFC8725 | IETF RFC 8725 JWT Best Current Practices | 2020 | مشروط به دامنه | 6 | [Official](https://www.rfc-editor.org/rfc/rfc8725.html) |
| OIDC | OpenID Connect Core | 1.0 with errata; verify current spec set | مشروط به دامنه | 26 | [Official](https://openid.net/specs/openid-connect-core-1_0.html) |
| PKCE_RFC7636 | IETF RFC 7636 PKCE | 2015 | مشروط به دامنه | 26 | [Official](https://www.rfc-editor.org/rfc/rfc7636.html) |
| COOKIE_RFC6265 | IETF RFC 6265 HTTP State Management Mechanism | 2011; track successor work | مستقیم/هسته‌ای | 15 | [Official](https://www.rfc-editor.org/rfc/rfc6265.html) |
| CSP_W3C | W3C Content Security Policy Level 3 | Living/current published spec; check status at use time | مستقیم/هسته‌ای | 18 | [Official](https://www.w3.org/TR/CSP/) |
| SRI_W3C | W3C Subresource Integrity | W3C specification | مستقیم/هسته‌ای | 18 | [Official](https://www.w3.org/TR/SRI/) |
| SARIF | OASIS SARIF | 2.1.0 + Approved Errata 01 | مستقیم/هسته‌ای | 32 | [Official](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) |
| CYCLONEDX | CycloneDX SBOM / supply-chain specification | 1.7 (ECMA-424) | پشتیبان/حاکمیتی | 18 | [Official](https://cyclonedx.org/specification/overview/) |
| SPDX | SPDX Software Package Data Exchange | 3.x specification family; pin schema in production | پشتیبان/حاکمیتی | 18 | [Official](https://spdx.dev/specifications/) |
| SLSA | Supply-chain Levels for Software Artifacts | 1.2 (approved) | پشتیبان/حاکمیتی | 70 | [Official](https://slsa.dev/spec/v1.2/) |
| OPENSSF_SCORECARD | OpenSSF Scorecard | Rolling checks | پشتیبان/حاکمیتی | 52 | [Official](https://openssf.org/scorecard/) |
| CWE_TOP25 | MITRE CWE Top 25 | 2025 | پشتیبان/حاکمیتی | 112 | [Official](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) |
| CAPEC | MITRE CAPEC | Current catalog | پشتیبان/حاکمیتی | 36 | [Official](https://capec.mitre.org/) |
| ATTACK | MITRE ATT&CK | Current enterprise/mobile/cloud knowledge bases | پشتیبان/حاکمیتی | 16 | [Official](https://attack.mitre.org/) |
| CVSS | FIRST Common Vulnerability Scoring System | 4.0 | پشتیبان/حاکمیتی | 47 | [Official](https://www.first.org/cvss/v4.0/) |
| EPSS | FIRST Exploit Prediction Scoring System | Rolling daily model | پشتیبان/حاکمیتی | 15 | [Official](https://www.first.org/epss/) |
| CISA_KEV | CISA Known Exploited Vulnerabilities Catalog | Rolling catalog | پشتیبان/حاکمیتی | 15 | [Official](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) |
| CIS_CONTROLS | CIS Critical Security Controls | v8.1 | پشتیبان/حاکمیتی | 85 | [Official](https://www.cisecurity.org/controls/v8-1) |
| CIS_BENCHMARKS | CIS Benchmarks | Product-specific rolling editions | مشروط به دامنه | 18 | [Official](https://www.cisecurity.org/cis-benchmarks) |
| CISA_SECURE_BY_DESIGN | CISA Secure by Design Pledge | Voluntary pledge | پشتیبان/حاکمیتی | 39 | [Official](https://www.cisa.gov/securebydesign) |
| FIPS1403 | FIPS 140-3 Cryptographic Module Validation | 2019 standard, CMVP program | مشروط به دامنه | 18 | [Official](https://csrc.nist.gov/pubs/fips/140-3/final) |
| ISO42001 | ISO/IEC 42001 AI Management System | 2023 | مشروط به دامنه | 14 | [Official](https://www.iso.org/standard/81230.html) |
| SLSA_PROVENANCE | in-toto / provenance attestations | Current specification ecosystem | پشتیبان/حاکمیتی | 52 | [Official](https://in-toto.io/) |

## خلاصه‌ی کنترل‌ها بر اساس حوزه

| شناسه حوزه | حوزه | تعداد |
|---|---|---:|
| GOV | Governance, authorization and scope | 20 |
| RISK | Risk assessment and threat modeling | 16 |
| ASSET | Asset inventory and attack-surface discovery | 15 |
| ARCH | Secure architecture and application design | 15 |
| AUTHN | Authentication, identity lifecycle and federation | 20 |
| AUTHZ | Authorization, tenancy and object-level access | 18 |
| SESSION | Session, cookies and browser state | 15 |
| INPUT | Input validation, output encoding and injection | 20 |
| API | API contracts, REST, GraphQL and RPC | 20 |
| WEB | HTTP, browser policies and web configuration | 18 |
| CRYPTO | Cryptography, certificates and secret management | 18 |
| DATA | Data protection, privacy and retention | 16 |
| FILES | Uploads, downloads, parsing and SSRF surfaces | 15 |
| BUSINESS | Business logic, automation abuse and resource limits | 15 |
| ERROR | Error handling, logging, detection and response | 15 |
| SDLC | Secure development lifecycle and verification | 20 |
| SUPPLY | Software supply chain, dependencies and artifacts | 18 |
| CLOUD | Cloud, container, Kubernetes and infrastructure as code | 18 |
| AVAIL | Availability, resilience, rate limiting and recovery | 15 |
| VULN | Vulnerability management, disclosure and remediation | 15 |
| PRIVREG | Privacy, legal and sectoral applicability review | 12 |
| ACCESS | Accessibility and inclusive product interface | 12 |
| MOBILE | Mobile application security (conditional) | 10 |
| AI | AI/LLM/agent security (conditional) | 14 |
| SCANNER | Security testing product / scanner assurance | 20 |
| EVIDENCE | Evidence integrity, reporting and audit trail | 12 |
| STANDARDS | Standards mapping and conformity governance | 12 |
| RELEASE | Release, operations, backup and product governance | 14 |
| ACCESSIBILITY_REG | Accessibility conformance governance | 4 |
| IDENTITY_PROTOCOLS | Identity protocol configuration and token lifecycle | 6 |
| HTTP_PROTOCOLS | Protocol correctness and edge cases | 6 |
| SUPPORT | Security support, customer communication and disclosure | 5 |

## چک‌لیست کامل و جزئی کنترل‌ها

هر کنترل شامل هدف، معیار پذیرش، شواهد مورد انتظار، روش راستی‌آزمایی، اولویت، سطح applicability، رابطه با مراجع و URLهای رسمی است. متن کنترل‌ها بازنویسی مستقل است و نباید به‌عنوان نقل‌قول بند استاندارد تلقی شود.

### GOV — Governance, authorization and scope (20 کنترل)

#### `FWPRO-GOV-001` — P0 / core
- **هدف کنترل:** Obtain written authorization covering target owners, domains, IP ranges, ports, environments, test dates and permitted methods.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Obtain written authorization covering target owners, domains, IP ranges, ports, environments, test dates and permitted methods.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-002` — P0 / core
- **هدف کنترل:** Maintain a signed scope register with explicit inclusions, exclusions, emergency contacts and approval expiry.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Maintain a signed scope register with explicit inclusions, exclusions, emergency contacts and approval expiry.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-003` — P0 / core
- **هدف کنترل:** Require explicit authorization acknowledgement before any scan job can enter the active queue.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Require explicit authorization acknowledgement before any scan job can enter the active queue.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-004` — P0 / core
- **هدف کنترل:** Define prohibited actions including destructive writes, credential attacks, denial of service and production data mutation.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define prohibited actions including destructive writes, credential attacks, denial of service and production data mutation.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-005` — P0 / core
- **هدف کنترل:** Document third-party hosting, CDN, SaaS and processor permissions before testing their assets.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document third-party hosting, CDN, SaaS and processor permissions before testing their assets.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-006` — P0 / core
- **هدف کنترل:** Set an approved testing window, time zone, notification path and stop condition for each engagement.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Set an approved testing window, time zone, notification path and stop condition for each engagement.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-007` — P0 / core
- **هدف کنترل:** Record the business owner, technical owner, tester, reviewer and incident contact for every assessment.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record the business owner, technical owner, tester, reviewer and incident contact for every assessment.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-008` — P0 / core
- **هدف کنترل:** Define an escalation workflow for suspected critical exposure or accidental sensitive-data discovery.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define an escalation workflow for suspected critical exposure or accidental sensitive-data discovery.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-009` — P0 / core
- **هدف کنترل:** Use least-privileged, dedicated test identities and never request production user passwords.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use least-privileged, dedicated test identities and never request production user passwords.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-010` — P0 / core
- **هدف کنترل:** Retain evidence of scope approval and any scope-change authorization in an auditable location.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Retain evidence of scope approval and any scope-change authorization in an auditable location.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-011` — P0 / core
- **هدف کنترل:** Define data handling, retention, deletion and report-sharing terms before collection begins.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define data handling, retention, deletion and report-sharing terms before collection begins.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-012` — P0 / core
- **هدف کنترل:** Review legal/regulatory restrictions and regional data-transfer requirements before scanning.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Review legal/regulatory restrictions and regional data-transfer requirements before scanning.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-013` — P0 / core
- **هدف کنترل:** Record target ownership verification and resolve ambiguous host ownership before testing.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record target ownership verification and resolve ambiguous host ownership before testing.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-014` — P0 / core
- **هدف کنترل:** Re-confirm scope when DNS, hosting, domain ownership or target environment changes materially.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Re-confirm scope when DNS, hosting, domain ownership or target environment changes materially.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-015` — P0 / core
- **هدف کنترل:** Define criteria for pausing or terminating a scan due to instability, rate-limit signals or owner request.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define criteria for pausing or terminating a scan due to instability, rate-limit signals or owner request.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-016` — P0 / core
- **هدف کنترل:** Document accepted risks with rationale, approver, compensating controls and expiration date.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document accepted risks with rationale, approver, compensating controls and expiration date.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-017` — P0 / core
- **هدف کنترل:** Separate assessment permissions from production administration permissions.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Separate assessment permissions from production administration permissions.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-018` — P0 / core
- **هدف کنترل:** Document the assessment methodology, coverage limits, assumptions and known blind spots.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document the assessment methodology, coverage limits, assumptions and known blind spots.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-019` — P0 / core
- **هدف کنترل:** Require independent review for high-impact findings and major scope exceptions.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Require independent review for high-impact findings and major scope exceptions.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-GOV-020` — P0 / core
- **هدف کنترل:** Keep a record of assessment start/end times, configuration, tool version and operator identity.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Keep a record of assessment start/end times, configuration, tool version and operator identity.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_CSF; ISO27001; ISO31000; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

### RISK — Risk assessment and threat modeling (16 کنترل)

#### `FWPRO-RISK-001` — P1 / core
- **هدف کنترل:** Maintain current system context, trust boundaries, data flows and external dependencies.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Maintain current system context, trust boundaries, data flows and external dependencies.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-002` — P1 / core
- **هدف کنترل:** Identify security objectives, business-critical workflows and unacceptable impacts.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Identify security objectives, business-critical workflows and unacceptable impacts.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-003` — P1 / core
- **هدف کنترل:** Record trust boundaries between browser, API, backend, data stores, third-party services and admin paths.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record trust boundaries between browser, API, backend, data stores, third-party services and admin paths.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-004` — P1 / core
- **هدف کنترل:** Threat-model authentication, authorization, uploads, webhooks, file processors and URL-fetching features.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Threat-model authentication, authorization, uploads, webhooks, file processors and URL-fetching features.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-005` — P1 / core
- **هدف کنترل:** Include abuse cases, insider misuse, automation/bot abuse and account/tenant takeover scenarios.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Include abuse cases, insider misuse, automation/bot abuse and account/tenant takeover scenarios.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-006` — P1 / core
- **هدف کنترل:** Track assumptions and unresolved questions in the threat model with owners and review dates.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Track assumptions and unresolved questions in the threat model with owners and review dates.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-007` — P1 / core
- **هدف کنترل:** Map important threats to defensive controls, tests, evidence and remediation tickets.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Map important threats to defensive controls, tests, evidence and remediation tickets.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-008` — P1 / core
- **هدف کنترل:** Review threat models after major architecture, identity, data-flow or third-party changes.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Review threat models after major architecture, identity, data-flow or third-party changes.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-009` — P1 / core
- **هدف کنترل:** Use a documented risk method that distinguishes impact, likelihood, confidence and business context.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use a documented risk method that distinguishes impact, likelihood, confidence and business context.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-010` — P1 / core
- **هدف کنترل:** Prioritize reachable, exploitable and business-critical exposures rather than relying only on raw severity.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Prioritize reachable, exploitable and business-critical exposures rather than relying only on raw severity.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-011` — P1 / core
- **هدف کنترل:** Identify crown-jewel data and the controls required around it.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Identify crown-jewel data and the controls required around it.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-012` — P1 / core
- **هدف کنترل:** Review failure modes caused by partial outages, dependency failures and degraded security controls.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Review failure modes caused by partial outages, dependency failures and degraded security controls.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-013` — P1 / core
- **هدف کنترل:** Assess multi-tenant boundaries and cross-tenant impact explicitly.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Assess multi-tenant boundaries and cross-tenant impact explicitly.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-014` — P1 / core
- **هدف کنترل:** Assess supply-chain and build pipeline threats in addition to runtime threats.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Assess supply-chain and build pipeline threats in addition to runtime threats.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-015` — P1 / core
- **هدف کنترل:** Record residual risk decisions and verify that compensating controls are operational.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record residual risk decisions and verify that compensating controls are operational.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

#### `FWPRO-RISK-016` — P1 / core
- **هدف کنترل:** Maintain a mapping from threat scenarios to ATT&CK/CAPEC where it adds actionable context.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Maintain a mapping from threat scenarios to ATT&CK/CAPEC where it adds actionable context.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; NIST_CSF; NIST_800_53; ISO27001; ISO31000; CAPEC; ATTACK`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [CAPEC](https://capec.mitre.org/) · [ATTACK](https://attack.mitre.org/)

### ASSET — Asset inventory and attack-surface discovery (15 کنترل)

#### `FWPRO-ASSET-001` — P1 / core
- **هدف کنترل:** Inventory in-scope hosts, ports, schemes, applications, APIs and known environment variants.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Inventory in-scope hosts, ports, schemes, applications, APIs and known environment variants.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-002` — P1 / core
- **هدف کنترل:** Discover links, forms, scripts, resources, route hints and API specifications within scope.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Discover links, forms, scripts, resources, route hints and API specifications within scope.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-003` — P1 / core
- **هدف کنترل:** Record HTTP method, path template, parameters, content type and observed authentication context per endpoint.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Record HTTP method, path template, parameters, content type and observed authentication context per endpoint.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-004` — P1 / core
- **هدف کنترل:** Identify production, staging, administrative, partner and legacy API versions separately.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Identify production, staging, administrative, partner and legacy API versions separately.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-005` — P1 / core
- **هدف کنترل:** Parse robots.txt and sitemap as discovery hints without treating either as authorization to test.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Parse robots.txt and sitemap as discovery hints without treating either as authorization to test.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-006` — P1 / core
- **هدف کنترل:** Track endpoint source (HTML, JavaScript, OpenAPI, browser observation, manual seed) and discovery timestamp.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Track endpoint source (HTML, JavaScript, OpenAPI, browser observation, manual seed) and discovery timestamp.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-007` — P1 / core
- **هدف کنترل:** Deduplicate URL and endpoint variants using canonicalization rules documented in the tool.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Deduplicate URL and endpoint variants using canonicalization rules documented in the tool.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-008` — P1 / core
- **هدف کنترل:** Detect technology indicators with confidence and avoid treating a banner as proof of version or vulnerability.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Detect technology indicators with confidence and avoid treating a banner as proof of version or vulnerability.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-009` — P1 / core
- **هدف کنترل:** Flag stale, undocumented, deprecated and duplicate APIs for owner review.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Flag stale, undocumented, deprecated and duplicate APIs for owner review.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-010` — P1 / core
- **هدف کنترل:** Compare current and prior inventories to identify newly exposed routes and assets.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Compare current and prior inventories to identify newly exposed routes and assets.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-011` — P1 / core
- **هدف کنترل:** Respect scope at every redirect, subresource, script-discovered URL and browser request.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Respect scope at every redirect, subresource, script-discovered URL and browser request.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-012` — P1 / core
- **هدف کنترل:** Exclude sensitive token/reset/signature query URLs from normal crawling and report output.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Exclude sensitive token/reset/signature query URLs from normal crawling and report output.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-013` — P1 / core
- **هدف کنترل:** Record discovery limits when authentication or JavaScript runtime access is unavailable.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Record discovery limits when authentication or JavaScript runtime access is unavailable.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-014` — P1 / core
- **هدف کنترل:** Review exposed source maps, debug paths and metadata without attempting unauthorized repository access.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Review exposed source maps, debug paths and metadata without attempting unauthorized repository access.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

#### `FWPRO-ASSET-015` — P1 / core
- **هدف کنترل:** Confirm all discovered third-party hosts are separately approved before any active request is sent.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Confirm all discovered third-party hosts are separately approved before any active request is sent.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; NIST_CSF; CIS_CONTROLS`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1)

### ARCH — Secure architecture and application design (15 کنترل)

#### `FWPRO-ARCH-001` — P1 / core
- **هدف کنترل:** Document secure architecture decisions and security-relevant design trade-offs.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document secure architecture decisions and security-relevant design trade-offs.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-002` — P1 / core
- **هدف کنترل:** Apply deny-by-default and least privilege across application layers and service identities.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Apply deny-by-default and least privilege across application layers and service identities.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-003` — P1 / core
- **هدف کنترل:** Keep authorization decisions server-side and independent from client-visible UI state.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Keep authorization decisions server-side and independent from client-visible UI state.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-004` — P1 / core
- **هدف کنترل:** Separate public routes, privileged administrative interfaces and internal service endpoints.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Separate public routes, privileged administrative interfaces and internal service endpoints.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-005` — P1 / core
- **هدف کنترل:** Define service-to-service trust and authenticate internal calls rather than trusting network position alone.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define service-to-service trust and authenticate internal calls rather than trusting network position alone.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-006` — P1 / core
- **هدف کنترل:** Avoid placing secrets, security decisions or privileged business rules in client-side code.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Avoid placing secrets, security decisions or privileged business rules in client-side code.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-007` — P1 / core
- **هدف کنترل:** Use explicit data ownership and tenant-context propagation across service boundaries.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use explicit data ownership and tenant-context propagation across service boundaries.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-008` — P1 / core
- **هدف کنترل:** Define safe error behavior and failure modes for unavailable identity, authorization and policy services.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define safe error behavior and failure modes for unavailable identity, authorization and policy services.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-009` — P1 / core
- **هدف کنترل:** Design idempotency and replay protections for actions with financial or irreversible effects.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Design idempotency and replay protections for actions with financial or irreversible effects.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-010` — P1 / core
- **هدف کنترل:** Design rate, quota and resource controls around business operations and expensive code paths.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Design rate, quota and resource controls around business operations and expensive code paths.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-011` — P1 / core
- **هدف کنترل:** Review use of caches, reverse proxies and CDNs for private or tenant-specific content leakage.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Review use of caches, reverse proxies and CDNs for private or tenant-specific content leakage.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-012` — P1 / core
- **هدف کنترل:** Use a secure-by-default configuration and require explicit opt-in for risky capabilities.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use a secure-by-default configuration and require explicit opt-in for risky capabilities.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-013` — P1 / core
- **هدف کنترل:** Document security boundaries around webhooks, URL previewers, importers and export generators.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document security boundaries around webhooks, URL previewers, importers and export generators.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-014` — P1 / core
- **هدف کنترل:** Review cryptographic design and key lifecycle before implementing custom cryptography.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Review cryptographic design and key lifecycle before implementing custom cryptography.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ARCH-015` — P1 / core
- **هدف کنترل:** Record threat model and abuse-case review approvals before high-risk features go live.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record threat model and abuse-case review approvals before high-risk features go live.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_SAMM; OWASP_TOP10; NIST_SSDF; NIST_800_53; ISO27034; ISO27001`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001)

### AUTHN — Authentication, identity lifecycle and federation (20 کنترل)

#### `FWPRO-AUTHN-001` — P0 / core
- **هدف کنترل:** Use secure authentication protocols and avoid bespoke password/token schemes.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use secure authentication protocols and avoid bespoke password/token schemes.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-002` — P0 / core
- **هدف کنترل:** Require multi-factor authentication for privileged and high-risk accounts where appropriate.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Require multi-factor authentication for privileged and high-risk accounts where appropriate.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-003` — P0 / core
- **هدف کنترل:** Protect password reset and account recovery with short-lived, single-use, purpose-bound tokens.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Protect password reset and account recovery with short-lived, single-use, purpose-bound tokens.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-004` — P0 / core
- **هدف کنترل:** Prevent account enumeration through consistent responses and timing where feasible.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Prevent account enumeration through consistent responses and timing where feasible.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-005` — P0 / core
- **هدف کنترل:** Apply rate limits and abuse controls to login, registration, recovery, OTP and verification endpoints.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Apply rate limits and abuse controls to login, registration, recovery, OTP and verification endpoints.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-006` — P0 / core
- **هدف کنترل:** Store passwords using a current, purpose-built password hashing scheme with suitable work factors and salts.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Store passwords using a current, purpose-built password hashing scheme with suitable work factors and salts.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-007` — P0 / core
- **هدف کنترل:** Reject breached or policy-prohibited credentials according to risk and organizational policy.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Reject breached or policy-prohibited credentials according to risk and organizational policy.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-008` — P0 / core
- **هدف کنترل:** Protect authentication responses against caching and accidental token disclosure.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Protect authentication responses against caching and accidental token disclosure.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-009` — P0 / core
- **هدف کنترل:** Rotate or invalidate sessions after login, privilege change, password reset and other security events.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Rotate or invalidate sessions after login, privilege change, password reset and other security events.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-010` — P0 / core
- **هدف کنترل:** Ensure logout and administrative revocation invalidate server-side state where required.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Ensure logout and administrative revocation invalidate server-side state where required.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-011` — P0 / core
- **هدف کنترل:** Validate issuer, audience, signature, expiry and intended use for JWTs and other assertions.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Validate issuer, audience, signature, expiry and intended use for JWTs and other assertions.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-012` — P0 / core
- **هدف کنترل:** Reject algorithm confusion, key substitution and unsigned token acceptance.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Reject algorithm confusion, key substitution and unsigned token acceptance.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-013` — P0 / core
- **هدف کنترل:** Use exact registered redirect URI matching for OAuth redirect-based flows.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use exact registered redirect URI matching for OAuth redirect-based flows.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-014` — P0 / core
- **هدف کنترل:** Use state and nonce protections appropriate to the selected OAuth/OIDC flow.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use state and nonce protections appropriate to the selected OAuth/OIDC flow.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-015` — P0 / core
- **هدف کنترل:** Require PKCE for applicable authorization-code clients and reject downgrade behavior.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Require PKCE for applicable authorization-code clients and reject downgrade behavior.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-016` — P0 / core
- **هدف کنترل:** Prevent open redirects from leaking authorization codes or tokens.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Prevent open redirects from leaking authorization codes or tokens.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-017` — P0 / core
- **هدف کنترل:** Protect refresh tokens with rotation or sender constraint when supported by the architecture.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Protect refresh tokens with rotation or sender constraint when supported by the architecture.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-018` — P0 / core
- **هدف کنترل:** Implement account lifecycle controls for provisioning, deprovisioning, lockout and recovery.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Implement account lifecycle controls for provisioning, deprovisioning, lockout and recovery.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-019` — P0 / core
- **هدف کنترل:** Use re-authentication or step-up checks for sensitive actions and changes to security settings.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use re-authentication or step-up checks for sensitive actions and changes to security settings.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

#### `FWPRO-AUTHN-020` — P0 / core
- **هدف کنترل:** Document intended assurance levels for identity proofing, authenticators and federated login.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document intended assurance levels for identity proofing, authenticators and federated login.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_63; NIST_800_53; ISO27002; OAUTH_RFC9700; OIDC; PKCE_RFC7636`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html)

### AUTHZ — Authorization, tenancy and object-level access (18 کنترل)

#### `FWPRO-AUTHZ-001` — P0 / core
- **هدف کنترل:** Enforce server-side authorization on every protected object, function and property access.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Enforce server-side authorization on every protected object, function and property access.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-002` — P0 / core
- **هدف کنترل:** Test horizontal access between two users with distinct, controlled test data.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test horizontal access between two users with distinct, controlled test data.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-003` — P0 / core
- **هدف کنترل:** Test vertical access across low-privilege, privileged and administrative roles.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test vertical access across low-privilege, privileged and administrative roles.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-004` — P0 / core
- **هدف کنترل:** Test tenant isolation across list, detail, search, export, report and bulk operations.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test tenant isolation across list, detail, search, export, report and bulk operations.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-005` — P0 / core
- **هدف کنترل:** Verify object ownership and tenant context are derived from trusted server-side identity, not request parameters alone.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Verify object ownership and tenant context are derived from trusted server-side identity, not request parameters alone.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-006` — P0 / core
- **هدف کنترل:** Apply field-level authorization to sensitive response properties and writable fields.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Apply field-level authorization to sensitive response properties and writable fields.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-007` — P0 / core
- **هدف کنترل:** Prevent mass assignment of role, owner, tenant, approval, price or internal status fields.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Prevent mass assignment of role, owner, tenant, approval, price or internal status fields.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-008` — P0 / core
- **هدف کنترل:** Ensure hidden endpoints and client-side route guards are not treated as authorization controls.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Ensure hidden endpoints and client-side route guards are not treated as authorization controls.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-009` — P0 / core
- **هدف کنترل:** Validate authorization before performing any state-changing side effect.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Validate authorization before performing any state-changing side effect.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-010` — P0 / core
- **هدف کنترل:** Check authorization for asynchronous jobs, exports, webhooks, file downloads and generated reports.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Check authorization for asynchronous jobs, exports, webhooks, file downloads and generated reports.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-011` — P0 / core
- **هدف کنترل:** Ensure authorization context cannot be confused across concurrent requests or shared caches.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Ensure authorization context cannot be confused across concurrent requests or shared caches.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-012` — P0 / core
- **هدف کنترل:** Define and test service-account permissions, API scopes and administrative boundaries.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define and test service-account permissions, API scopes and administrative boundaries.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-013` — P0 / core
- **هدف کنترل:** Review group/role inheritance and deny/allow precedence for least privilege.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Review group/role inheritance and deny/allow precedence for least privilege.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-014` — P0 / core
- **هدف کنترل:** Test direct object identifiers only with authorized test accounts and non-sensitive fixtures.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test direct object identifiers only with authorized test accounts and non-sensitive fixtures.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-015` — P0 / core
- **هدف کنترل:** Record expected-versus-actual outcomes and sanitized evidence for every authorization test.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record expected-versus-actual outcomes and sanitized evidence for every authorization test.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-016` — P0 / core
- **هدف کنترل:** Treat automated role-difference results as review candidates until object ownership and business context are verified.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Treat automated role-difference results as review candidates until object ownership and business context are verified.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-017` — P0 / core
- **هدف کنترل:** Confirm default policy for unknown roles, missing claims and malformed authorization context is deny.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Confirm default policy for unknown roles, missing claims and malformed authorization context is deny.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-AUTHZ-018` — P0 / core
- **هدف کنترل:** Re-test authorization after role, tenant, API schema or route changes.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Re-test authorization after role, tenant, API schema or route changes.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_800_53; NIST_800_63; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

### SESSION — Session, cookies and browser state (15 کنترل)

#### `FWPRO-SESSION-001` — P1 / core
- **هدف کنترل:** Set Secure on session cookies in HTTPS deployments.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Set Secure on session cookies in HTTPS deployments.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-002` — P1 / core
- **هدف کنترل:** Set HttpOnly on cookies that do not require direct JavaScript access.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Set HttpOnly on cookies that do not require direct JavaScript access.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-003` — P1 / core
- **هدف کنترل:** Choose SameSite deliberately based on application flows and CSRF threat model.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Choose SameSite deliberately based on application flows and CSRF threat model.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-004` — P1 / core
- **هدف کنترل:** Use cookie prefixes and path/domain constraints where they add enforceable protection.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Use cookie prefixes and path/domain constraints where they add enforceable protection.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-005` — P1 / core
- **هدف کنترل:** Avoid unnecessarily broad cookie Domain and Path scope.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Avoid unnecessarily broad cookie Domain and Path scope.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-006` — P1 / core
- **هدف کنترل:** Rotate identifiers after authentication and privilege changes.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Rotate identifiers after authentication and privilege changes.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-007` — P1 / core
- **هدف کنترل:** Enforce idle and absolute session expiration appropriate to data sensitivity.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Enforce idle and absolute session expiration appropriate to data sensitivity.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-008` — P1 / core
- **هدف کنترل:** Invalidate server-side sessions on logout, revocation and account compromise events.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Invalidate server-side sessions on logout, revocation and account compromise events.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-009` — P1 / core
- **هدف کنترل:** Protect state-changing requests with CSRF defenses appropriate to the authentication model.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Protect state-changing requests with CSRF defenses appropriate to the authentication model.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-010` — P1 / core
- **هدف کنترل:** Check Origin/Referer or equivalent request provenance where appropriate, without treating it as the only CSRF control.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Check Origin/Referer or equivalent request provenance where appropriate, without treating it as the only CSRF control.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-011` — P1 / core
- **هدف کنترل:** Do not cache authenticated sensitive pages publicly or across tenants.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Do not cache authenticated sensitive pages publicly or across tenants.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-012` — P1 / core
- **هدف کنترل:** Ensure tokens are not exposed in URLs, browser history, referrers, telemetry or error pages.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Ensure tokens are not exposed in URLs, browser history, referrers, telemetry or error pages.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-013` — P1 / core
- **هدف کنترل:** Avoid storing high-value session secrets in localStorage when safer alternatives meet the architecture.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Avoid storing high-value session secrets in localStorage when safer alternatives meet the architecture.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-014` — P1 / core
- **هدف کنترل:** Review concurrent session handling and suspicious-session revocation.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Review concurrent session handling and suspicious-session revocation.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-SESSION-015` — P1 / core
- **هدف کنترل:** Test session behavior in a real browser for applicable SameSite and cross-origin interactions.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Test session behavior in a real browser for applicable SameSite and cross-origin interactions.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_CHEATSHEETS; COOKIE_RFC6265; OWASP_TOP10; NIST_800_63; NIST_800_53`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [COOKIE_RFC6265](https://www.rfc-editor.org/rfc/rfc6265.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

### INPUT — Input validation, output encoding and injection (20 کنترل)

#### `FWPRO-INPUT-001` — P0 / core
- **هدف کنترل:** Validate inputs with allowlists, type constraints, canonicalization and size limits at trusted boundaries.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Validate inputs with allowlists, type constraints, canonicalization and size limits at trusted boundaries.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-002` — P0 / core
- **هدف کنترل:** Use context-appropriate output encoding for HTML, attributes, JavaScript, CSS and URL contexts.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use context-appropriate output encoding for HTML, attributes, JavaScript, CSS and URL contexts.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-003` — P0 / core
- **هدف کنترل:** Use safe DOM APIs and avoid interpreting untrusted strings as executable markup or script.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use safe DOM APIs and avoid interpreting untrusted strings as executable markup or script.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-004` — P0 / core
- **هدف کنترل:** Use parameterized database queries or equivalent safe query construction.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use parameterized database queries or equivalent safe query construction.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-005` — P0 / core
- **هدف کنترل:** Review SQL, NoSQL, LDAP, XPath and search-query construction for interpreter injection.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Review SQL, NoSQL, LDAP, XPath and search-query construction for interpreter injection.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-006` — P0 / core
- **هدف کنترل:** Use safe process APIs without shell interpolation for operating-system operations.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use safe process APIs without shell interpolation for operating-system operations.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-007` — P0 / core
- **هدف کنترل:** Review template rendering to ensure untrusted data cannot become executable template syntax.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Review template rendering to ensure untrusted data cannot become executable template syntax.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-008` — P0 / core
- **هدف کنترل:** Disable unsafe XML external entity and external resource resolution where not required.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Disable unsafe XML external entity and external resource resolution where not required.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-009` — P0 / core
- **هدف کنترل:** Validate file paths after canonicalization and enforce containment within an approved directory.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Validate file paths after canonicalization and enforce containment within an approved directory.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-010` — P0 / core
- **هدف کنترل:** Validate URL-fetch inputs against scheme, hostname, port, DNS and network policy to reduce SSRF risk.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Validate URL-fetch inputs against scheme, hostname, port, DNS and network policy to reduce SSRF risk.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-011` — P0 / core
- **هدف کنترل:** Prevent HTTP parameter pollution and duplicate-parameter ambiguity in security-sensitive inputs.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Prevent HTTP parameter pollution and duplicate-parameter ambiguity in security-sensitive inputs.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-012` — P0 / core
- **هدف کنترل:** Set maximum request, header, body, nesting, decompression and parser sizes.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Set maximum request, header, body, nesting, decompression and parser sizes.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-013` — P0 / core
- **هدف کنترل:** Validate Unicode, null byte, control character and alternate-encoding edge cases.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Validate Unicode, null byte, control character and alternate-encoding edge cases.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-014` — P0 / core
- **هدف کنترل:** Ensure validation and authorization occur on the server for every input path.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Ensure validation and authorization occur on the server for every input path.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-015` — P0 / core
- **هدف کنترل:** Use safe deserialization formats and reject unexpected polymorphic/object types.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use safe deserialization formats and reject unexpected polymorphic/object types.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-016` — P0 / core
- **هدف کنترل:** Avoid dynamic code evaluation and unsafe expression-language execution on user-controlled content.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Avoid dynamic code evaluation and unsafe expression-language execution on user-controlled content.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-017` — P0 / core
- **هدف کنترل:** Review regular expressions and parsing logic for catastrophic backtracking or algorithmic complexity.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Review regular expressions and parsing logic for catastrophic backtracking or algorithmic complexity.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-018` — P0 / core
- **هدف کنترل:** Test reflected parameter canaries as observations only; require safe context validation before declaring XSS.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Test reflected parameter canaries as observations only; require safe context validation before declaring XSS.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-019` — P0 / core
- **هدف کنترل:** Confirm error messages do not echo raw dangerous input or secrets into executable output contexts.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Confirm error messages do not echo raw dangerous input or secrets into executable output contexts.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

#### `FWPRO-INPUT-020` — P0 / core
- **هدف کنترل:** Record tests requiring active payloads as manual/specialist-tool tasks rather than silently claiming coverage.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Record tests requiring active payloads as manual/specialist-tool tasks rather than silently claiming coverage.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_CHEATSHEETS; CWE_TOP25; CAPEC; OWASP_API`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CAPEC](https://capec.mitre.org/) · [OWASP_API](https://owasp.org/www-project-api-security/)

### API — API contracts, REST, GraphQL and RPC (20 کنترل)

#### `FWPRO-API-001` — P0 / core
- **هدف کنترل:** Maintain an authoritative API inventory with owners, versions, environments and deprecation state.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Maintain an authoritative API inventory with owners, versions, environments and deprecation state.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-002` — P0 / core
- **هدف کنترل:** Validate OpenAPI documents against the declared supported specification version and schema.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Validate OpenAPI documents against the declared supported specification version and schema.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-003` — P0 / core
- **هدف کنترل:** Declare authentication and security requirements at the appropriate API/operation levels.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Declare authentication and security requirements at the appropriate API/operation levels.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-004` — P0 / core
- **هدف کنترل:** Check for operations accidentally marked public where authentication is expected.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Check for operations accidentally marked public where authentication is expected.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-005` — P0 / core
- **هدف کنترل:** Document request and response schemas, constraints, error formats and sensitive fields.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Document request and response schemas, constraints, error formats and sensitive fields.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-006` — P0 / core
- **هدف کنترل:** Apply object-level authorization to endpoints accepting object identifiers.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Apply object-level authorization to endpoints accepting object identifiers.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-007` — P0 / core
- **هدف کنترل:** Apply function-level and property-level authorization to API operations and data fields.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Apply function-level and property-level authorization to API operations and data fields.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-008` — P0 / core
- **هدف کنترل:** Limit page size, batch count, query complexity, upload size and expensive operations.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Limit page size, batch count, query complexity, upload size and expensive operations.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-009` — P0 / core
- **هدف کنترل:** Use quotas/rate limits and abuse protections for business-sensitive or expensive API workflows.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Use quotas/rate limits and abuse protections for business-sensitive or expensive API workflows.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-010` — P0 / core
- **هدف کنترل:** Disable or restrict introspection/schema exploration according to documented GraphQL policy.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Disable or restrict introspection/schema exploration according to documented GraphQL policy.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-011` — P0 / core
- **هدف کنترل:** Control GraphQL depth, alias count, batching and query cost when exposed to untrusted clients.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Control GraphQL depth, alias count, batching and query cost when exposed to untrusted clients.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-012` — P0 / core
- **هدف کنترل:** Validate GraphQL resolver authorization independently of schema visibility.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Validate GraphQL resolver authorization independently of schema visibility.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-013` — P0 / core
- **هدف کنترل:** Authenticate and authorize WebSocket, SSE, gRPC and other non-REST channels where present.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Authenticate and authorize WebSocket, SSE, gRPC and other non-REST channels where present.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-014` — P0 / core
- **هدف کنترل:** Handle content types, methods, CORS preflight and unsupported methods consistently.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Handle content types, methods, CORS preflight and unsupported methods consistently.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-015` — P0 / core
- **هدف کنترل:** Prevent undocumented debug, legacy and shadow API versions from remaining unnecessarily accessible.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Prevent undocumented debug, legacy and shadow API versions from remaining unnecessarily accessible.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-016` — P0 / core
- **هدف کنترل:** Validate webhook signatures, replay windows, source authenticity and event authorization.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Validate webhook signatures, replay windows, source authenticity and event authorization.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-017` — P0 / core
- **هدف کنترل:** Validate response filtering so internal fields, tokens and cross-tenant data are not exposed.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Validate response filtering so internal fields, tokens and cross-tenant data are not exposed.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-018` — P0 / core
- **هدف کنترل:** Version API security behavior and define compatible deprecation/removal policy.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Version API security behavior and define compatible deprecation/removal policy.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-019` — P0 / core
- **هدف کنترل:** Treat API discovery as inventory evidence, not proof that every business operation has been tested.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Treat API discovery as inventory evidence, not proof that every business operation has been tested.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-API-020` — P0 / core
- **هدف کنترل:** Use test accounts and synthetic records for destructive or state-changing business API verification.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Use test accounts and synthetic records for destructive or state-changing business API verification.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ASVS; OWASP_WSTG; OPENAPI; JSON_SCHEMA; HTTP_RFC9110; OWASP_TOP10; CWE_TOP25`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OPENAPI](https://spec.openapis.org/oas/) · [JSON_SCHEMA](https://json-schema.org/specification) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

### WEB — HTTP, browser policies and web configuration (18 کنترل)

#### `FWPRO-WEB-001` — P1 / core
- **هدف کنترل:** Redirect HTTP to HTTPS without loops or downgrade paths for production sites.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Redirect HTTP to HTTPS without loops or downgrade paths for production sites.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-002` — P1 / core
- **هدف کنترل:** Apply an HSTS policy only after HTTPS coverage and subdomain implications are understood.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Apply an HSTS policy only after HTTPS coverage and subdomain implications are understood.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-003` — P1 / core
- **هدف کنترل:** Deploy a CSP appropriate to the application and avoid unsafe directives when feasible.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Deploy a CSP appropriate to the application and avoid unsafe directives when feasible.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-004` — P1 / core
- **هدف کنترل:** Review frame-ancestors or equivalent clickjacking protections for sensitive interfaces.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Review frame-ancestors or equivalent clickjacking protections for sensitive interfaces.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-005` — P1 / core
- **هدف کنترل:** Set X-Content-Type-Options to prevent MIME sniffing where applicable.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Set X-Content-Type-Options to prevent MIME sniffing where applicable.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-006` — P1 / core
- **هدف کنترل:** Set a Referrer-Policy consistent with privacy and functional requirements.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Set a Referrer-Policy consistent with privacy and functional requirements.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-007` — P1 / core
- **هدف کنترل:** Set Permissions-Policy to disable unused sensitive browser capabilities where feasible.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Set Permissions-Policy to disable unused sensitive browser capabilities where feasible.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-008` — P1 / core
- **هدف کنترل:** Review COOP, COEP and CORP where cross-origin isolation/resource isolation is required.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Review COOP, COEP and CORP where cross-origin isolation/resource isolation is required.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-009` — P1 / core
- **هدف کنترل:** Ensure security headers are consistently applied on success, error, authentication and redirect responses.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Ensure security headers are consistently applied on success, error, authentication and redirect responses.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-010` — P1 / core
- **هدف کنترل:** Avoid leaking server/framework versions and internal host names in response banners.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Avoid leaking server/framework versions and internal host names in response banners.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-011` — P1 / core
- **هدف کنترل:** Review cache-control behavior for authenticated and sensitive pages.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Review cache-control behavior for authenticated and sensitive pages.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-012` — P1 / core
- **هدف کنترل:** Ensure security-sensitive redirects use allowlisted destinations and safe URL parsing.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Ensure security-sensitive redirects use allowlisted destinations and safe URL parsing.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-013` — P1 / core
- **هدف کنترل:** Check content-type correctness and avoid returning active content from untrusted upload hosts.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Check content-type correctness and avoid returning active content from untrusted upload hosts.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-014` — P1 / core
- **هدف کنترل:** Ensure error pages do not expose stack traces, configuration, paths or personal data.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Ensure error pages do not expose stack traces, configuration, paths or personal data.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-015` — P1 / core
- **هدف کنترل:** Review CORS origins, credential flags, methods and allowed headers against explicit business requirements.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Review CORS origins, credential flags, methods and allowed headers against explicit business requirements.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-016` — P1 / core
- **هدف کنترل:** Do not reflect arbitrary Origin values into access-control headers.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Do not reflect arbitrary Origin values into access-control headers.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-017` — P1 / core
- **هدف کنترل:** Use SRI for eligible immutable third-party scripts/styles and review update/rotation processes.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Use SRI for eligible immutable third-party scripts/styles and review update/rotation processes.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

#### `FWPRO-WEB-018` — P1 / core
- **هدف کنترل:** Avoid mixed content and insecure resource references in HTTPS pages.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Avoid mixed content and insecure resource references in HTTPS pages.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** direct
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; HTTP_RFC9110; HSTS_RFC6797; CSP_W3C; SRI_W3C`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [HSTS_RFC6797](https://www.rfc-editor.org/rfc/rfc6797.html) · [CSP_W3C](https://www.w3.org/TR/CSP/) · [SRI_W3C](https://www.w3.org/TR/SRI/)

### CRYPTO — Cryptography, certificates and secret management (18 کنترل)

#### `FWPRO-CRYPTO-001` — P0 / core
- **هدف کنترل:** Disable obsolete TLS versions and weak cipher suites according to current platform guidance.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Disable obsolete TLS versions and weak cipher suites according to current platform guidance.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-002` — P0 / core
- **هدف کنترل:** Prefer TLS 1.3 and maintain a documented compatibility exception for any TLS 1.2 dependency.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Prefer TLS 1.3 and maintain a documented compatibility exception for any TLS 1.2 dependency.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-003` — P0 / core
- **هدف کنترل:** Validate certificate chain, hostname, expiration, validity dates and renewal ownership.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Validate certificate chain, hostname, expiration, validity dates and renewal ownership.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-004` — P0 / core
- **هدف کنترل:** Protect private keys and signing keys from source code, logs, images and user-facing artifacts.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Protect private keys and signing keys from source code, logs, images and user-facing artifacts.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-005` — P0 / core
- **هدف کنترل:** Use a managed secret store with access controls, rotation and audit for production secrets.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Use a managed secret store with access controls, rotation and audit for production secrets.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-006` — P0 / core
- **هدف کنترل:** Separate development, staging and production keys and credentials.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Separate development, staging and production keys and credentials.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-007` — P0 / core
- **هدف کنترل:** Define cryptographic key creation, distribution, rotation, revocation, backup and destruction processes.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Define cryptographic key creation, distribution, rotation, revocation, backup and destruction processes.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-008` — P0 / core
- **هدف کنترل:** Use vetted cryptographic libraries and avoid custom algorithms or ad hoc modes.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Use vetted cryptographic libraries and avoid custom algorithms or ad hoc modes.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-009` — P0 / core
- **هدف کنترل:** Protect sensitive data in transit and at rest based on data classification and threat model.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Protect sensitive data in transit and at rest based on data classification and threat model.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-010` — P0 / core
- **هدف کنترل:** Use authenticated encryption or approved constructions when encrypting application data.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Use authenticated encryption or approved constructions when encrypting application data.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-011` — P0 / core
- **هدف کنترل:** Review random number generation and token generation for cryptographic suitability.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Review random number generation and token generation for cryptographic suitability.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-012` — P0 / core
- **هدف کنترل:** Ensure password hashes use a dedicated password-hashing scheme, not general-purpose hashes alone.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Ensure password hashes use a dedicated password-hashing scheme, not general-purpose hashes alone.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-013` — P0 / core
- **هدف کنترل:** Prevent tokens and secrets from appearing in query strings, referer headers, telemetry and reports.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Prevent tokens and secrets from appearing in query strings, referer headers, telemetry and reports.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-014` — P0 / core
- **هدف کنترل:** Define handling for certificates, signing keys and API tokens exposed in browser-delivered assets.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Define handling for certificates, signing keys and API tokens exposed in browser-delivered assets.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-015` — P0 / core
- **هدف کنترل:** Use validated cryptographic modules only when FIPS or another validation requirement explicitly applies.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Use validated cryptographic modules only when FIPS or another validation requirement explicitly applies.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-016` — P0 / core
- **هدف کنترل:** Monitor certificate/key expiry and test renewal before production expiry dates.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Monitor certificate/key expiry and test renewal before production expiry dates.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-017` — P0 / core
- **هدف کنترل:** Test secure failure behavior when key management or cryptographic services are unavailable.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Test secure failure behavior when key management or cryptographic services are unavailable.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

#### `FWPRO-CRYPTO-018` — P0 / core
- **هدف کنترل:** Record TLS settings and certificate chain evidence with time, hostname and scanner version.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Record TLS settings and certificate chain evidence with time, hostname and scanner version.
- **شواهد مورد انتظار:** Timestamped HTTP/browser observation, sanitized response/request metadata, scanner version and rule ID.
- **روش راستی‌آزمایی:** `automated_passive`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; NIST_800_53; ISO27002; TLS_RFC8446; TLS_BCP; FIPS1403`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27002](https://www.iso.org/standard/75652.html) · [TLS_RFC8446](https://www.rfc-editor.org/rfc/rfc8446.html) · [TLS_BCP](https://www.rfc-editor.org/rfc/rfc9852.html) · [FIPS1403](https://csrc.nist.gov/pubs/fips/140-3/final)

### DATA — Data protection, privacy and retention (16 کنترل)

#### `FWPRO-DATA-001` — P1 / core
- **هدف کنترل:** Maintain data inventory and classification for personal, payment, authentication and business-sensitive information.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Maintain data inventory and classification for personal, payment, authentication and business-sensitive information.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-002` — P1 / core
- **هدف کنترل:** Minimize personal and sensitive data collected, returned, logged and retained.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Minimize personal and sensitive data collected, returned, logged and retained.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-003` — P1 / core
- **هدف کنترل:** Document data purpose, legal basis and retention requirements where privacy law applies.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document data purpose, legal basis and retention requirements where privacy law applies.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-004` — P1 / core
- **هدف کنترل:** Limit access to personal and regulated data by role, purpose and tenant.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Limit access to personal and regulated data by role, purpose and tenant.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-005` — P1 / core
- **هدف کنترل:** Mask or redact sensitive data in logs, telemetry, error pages, exports and security reports.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Mask or redact sensitive data in logs, telemetry, error pages, exports and security reports.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-006` — P1 / core
- **هدف کنترل:** Verify deletion and retention processes for user records, exports, backups and derived artifacts.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Verify deletion and retention processes for user records, exports, backups and derived artifacts.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-007` — P1 / core
- **هدف کنترل:** Ensure exports and downloadable reports enforce authorization and expire or revoke access when needed.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Ensure exports and downloadable reports enforce authorization and expire or revoke access when needed.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-008` — P1 / core
- **هدف کنترل:** Use pseudonymization or aggregation in test fixtures wherever practical.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use pseudonymization or aggregation in test fixtures wherever practical.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-009` — P1 / core
- **هدف کنترل:** Avoid production personal data in ordinary development/test environments.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Avoid production personal data in ordinary development/test environments.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-010` — P1 / core
- **هدف کنترل:** Document processor/subprocessor roles, hosting locations and international transfers where applicable.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document processor/subprocessor roles, hosting locations and international transfers where applicable.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-011` — P1 / core
- **هدف کنترل:** Provide mechanisms for data-subject requests where legally required and applicable.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Provide mechanisms for data-subject requests where legally required and applicable.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-012` — P1 / core
- **هدف کنترل:** Assess privacy risks for new high-risk processing and document DPIA decisions where required.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Assess privacy risks for new high-risk processing and document DPIA decisions where required.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-013` — P1 / core
- **هدف کنترل:** Protect report files at rest and use a defined retention/deletion window.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Protect report files at rest and use a defined retention/deletion window.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-014` — P1 / core
- **هدف کنترل:** Prevent secrets or high-sensitivity evidence from being included in analytics by default.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Prevent secrets or high-sensitivity evidence from being included in analytics by default.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-015` — P1 / core
- **هدف کنترل:** Define rules for handling accidental exposure of credentials, health records, payment data or other sensitive evidence.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define rules for handling accidental exposure of credentials, health records, payment data or other sensitive evidence.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

#### `FWPRO-DATA-016` — P1 / core
- **هدف کنترل:** Review response bodies and browser storage for unintended data disclosure with authorized accounts.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Review response bodies and browser storage for unintended data disclosure with authorized accounts.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; NIST_PRIVACY; NIST_800_53; ISO27701; GDPR; HIPAA; PCI_DSS`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27701](https://www.iso.org/standard/27701) · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/)

### FILES — Uploads, downloads, parsing and SSRF surfaces (15 کنترل)

#### `FWPRO-FILES-001` — P1 / conditional
- **هدف کنترل:** Allowlist upload types using content inspection in addition to user-supplied extension and MIME type.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Allowlist upload types using content inspection in addition to user-supplied extension and MIME type.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-002` — P1 / conditional
- **هدف کنترل:** Limit file size, count, decompression ratio, nesting depth and processing time.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Limit file size, count, decompression ratio, nesting depth and processing time.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-003` — P1 / conditional
- **هدف کنترل:** Store untrusted uploads outside executable web roots with restrictive permissions.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Store untrusted uploads outside executable web roots with restrictive permissions.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-004` — P1 / conditional
- **هدف کنترل:** Generate server-side storage names and prevent path traversal through supplied file names.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Generate server-side storage names and prevent path traversal through supplied file names.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-005` — P1 / conditional
- **هدف کنترل:** Scan or sandbox risky content before downstream use when justified by the threat model.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Scan or sandbox risky content before downstream use when justified by the threat model.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-006` — P1 / conditional
- **هدف کنترل:** Prevent uploaded active content from sharing a trusted origin with authenticated application pages.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Prevent uploaded active content from sharing a trusted origin with authenticated application pages.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-007` — P1 / conditional
- **هدف کنترل:** Set safe Content-Disposition and content types for file downloads.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Set safe Content-Disposition and content types for file downloads.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-008` — P1 / conditional
- **هدف کنترل:** Authorize file access independently of guessed or enumerated file identifiers.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Authorize file access independently of guessed or enumerated file identifiers.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-009` — P1 / conditional
- **هدف کنترل:** Validate archive extraction against path traversal, symlink escape and zip-bomb behavior.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Validate archive extraction against path traversal, symlink escape and zip-bomb behavior.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-010` — P1 / conditional
- **هدف کنترل:** Disable unsafe XML external entity and external schema fetching in parsers that do not need them.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Disable unsafe XML external entity and external schema fetching in parsers that do not need them.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-011` — P1 / conditional
- **هدف کنترل:** Use outbound request allowlists and egress network controls for URL-fetching functions.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use outbound request allowlists and egress network controls for URL-fetching functions.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-012` — P1 / conditional
- **هدف کنترل:** Resolve and validate DNS/IP destinations at connection time to mitigate SSRF and rebinding.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Resolve and validate DNS/IP destinations at connection time to mitigate SSRF and rebinding.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-013` — P1 / conditional
- **هدف کنترل:** Block loopback, link-local, private, multicast and metadata-service destinations unless explicitly required and isolated.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Block loopback, link-local, private, multicast and metadata-service destinations unless explicitly required and isolated.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-014` — P1 / conditional
- **هدف کنترل:** Limit redirects, schemes, ports, response sizes and timeouts in URL fetchers.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Limit redirects, schemes, ports, response sizes and timeouts in URL fetchers.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-FILES-015` — P1 / conditional
- **هدف کنترل:** Use safe parsers for image, document, PDF and media processing; isolate high-risk converters.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use safe parsers for image, document, PDF and media processing; isolate high-risk converters.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_API; OWASP_CHEATSHEETS; CWE_TOP25`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

### BUSINESS — Business logic, automation abuse and resource limits (15 کنترل)

#### `FWPRO-BUSINESS-001` — P1 / conditional
- **هدف کنترل:** Define expected state transitions and reject illegal workflow transitions server-side.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define expected state transitions and reject illegal workflow transitions server-side.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-002` — P1 / conditional
- **هدف کنترل:** Test price, quantity, discount, tax, currency and rounding rules with synthetic accounts/data.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test price, quantity, discount, tax, currency and rounding rules with synthetic accounts/data.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-003` — P1 / conditional
- **هدف کنترل:** Use idempotency controls for retryable payment, order, provisioning and sensitive transaction APIs.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use idempotency controls for retryable payment, order, provisioning and sensitive transaction APIs.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-004` — P1 / conditional
- **هدف کنترل:** Ensure approval steps cannot be skipped by direct API calls or altered client state.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Ensure approval steps cannot be skipped by direct API calls or altered client state.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-005` — P1 / conditional
- **هدف کنترل:** Define rate, quota and concurrency limits for account creation, recovery, search and expensive workflows.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define rate, quota and concurrency limits for account creation, recovery, search and expensive workflows.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-006` — P1 / conditional
- **هدف کنترل:** Detect and mitigate scraping, credential stuffing, scalping, fake-account creation and resource hoarding where relevant.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Detect and mitigate scraping, credential stuffing, scalping, fake-account creation and resource hoarding where relevant.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-007` — P1 / conditional
- **هدف کنترل:** Prevent replay of signed requests, webhooks, invitations and one-time actions beyond allowed windows.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Prevent replay of signed requests, webhooks, invitations and one-time actions beyond allowed windows.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-008` — P1 / conditional
- **هدف کنترل:** Verify workflow ownership and role authorization across every step, not just entry pages.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Verify workflow ownership and role authorization across every step, not just entry pages.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-009` — P1 / conditional
- **هدف کنترل:** Test abuse of cancellations, refunds, coupons, referral credits and trial/entitlement logic with test fixtures.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test abuse of cancellations, refunds, coupons, referral credits and trial/entitlement logic with test fixtures.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-010` — P1 / conditional
- **هدف کنترل:** Ensure race conditions cannot bypass balance, stock, quota or approval invariants.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Ensure race conditions cannot bypass balance, stock, quota or approval invariants.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-011` — P1 / conditional
- **هدف کنترل:** Document business-sensitive actions that require human review, step-up authentication or additional telemetry.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document business-sensitive actions that require human review, step-up authentication or additional telemetry.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-012` — P1 / conditional
- **هدف کنترل:** Avoid high-volume or destructive tests on production; use staging and owner-approved synthetic datasets.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Avoid high-volume or destructive tests on production; use staging and owner-approved synthetic datasets.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-013` — P1 / conditional
- **هدف کنترل:** Check that expensive endpoints have bounded compute, result sizes and database work.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Check that expensive endpoints have bounded compute, result sizes and database work.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-014` — P1 / conditional
- **هدف کنترل:** Record business-owner validation for candidate risks that cannot be judged from HTTP response behavior alone.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record business-owner validation for candidate risks that cannot be judged from HTTP response behavior alone.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-BUSINESS-015` — P1 / conditional
- **هدف کنترل:** Define bot detection controls with privacy review and documented false-positive handling where applicable.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define bot detection controls with privacy review and documented false-positive handling where applicable.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; OWASP_API; OWASP_ATWA; OWASP_TOP10; NIST_CSF; ISO31000`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO31000](https://www.iso.org/standard/65694.html)

### ERROR — Error handling, logging, detection and response (15 کنترل)

#### `FWPRO-ERROR-001` — P1 / core
- **هدف کنترل:** Return generic client-facing errors while preserving useful, access-controlled server diagnostics.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Return generic client-facing errors while preserving useful, access-controlled server diagnostics.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-002` — P1 / core
- **هدف کنترل:** Never log passwords, access tokens, session identifiers, private keys or unredacted authorization headers.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Never log passwords, access tokens, session identifiers, private keys or unredacted authorization headers.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-003` — P1 / core
- **هدف کنترل:** Log security-relevant authentication, authorization, privilege, configuration and administrative events.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Log security-relevant authentication, authorization, privilege, configuration and administrative events.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-004` — P1 / core
- **هدف کنترل:** Protect logs against unauthorized access, tampering, truncation and uncontrolled retention.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Protect logs against unauthorized access, tampering, truncation and uncontrolled retention.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-005` — P1 / core
- **هدف کنترل:** Use reliable timestamps/time synchronization and correlate events across services.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use reliable timestamps/time synchronization and correlate events across services.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-006` — P1 / core
- **هدف کنترل:** Alert on high-risk events and define response ownership and escalation timeframes.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Alert on high-risk events and define response ownership and escalation timeframes.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-007` — P1 / core
- **هدف کنترل:** Test alert delivery and incident response with safe tabletop exercises.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test alert delivery and incident response with safe tabletop exercises.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-008` — P1 / core
- **هدف کنترل:** Maintain incident response procedures for credential exposure, data leakage and critical vulnerability discovery.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Maintain incident response procedures for credential exposure, data leakage and critical vulnerability discovery.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-009` — P1 / core
- **هدف کنترل:** Document evidence-preservation and chain-of-custody practices for investigations.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document evidence-preservation and chain-of-custody practices for investigations.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-010` — P1 / core
- **هدف کنترل:** Define how security findings are classified, assigned, tracked, accepted and closed.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define how security findings are classified, assigned, tracked, accepted and closed.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-011` — P1 / core
- **هدف کنترل:** Test that log contents are sanitized against CR/LF and structured-log injection.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test that log contents are sanitized against CR/LF and structured-log injection.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-012` — P1 / core
- **هدف کنترل:** Separate operational logs from security audit events where required by assurance needs.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Separate operational logs from security audit events where required by assurance needs.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-013` — P1 / core
- **هدف کنترل:** Use monitoring to detect abnormal rates, unusual role changes and suspicious business workflows.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use monitoring to detect abnormal rates, unusual role changes and suspicious business workflows.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-014` — P1 / core
- **هدف کنترل:** Maintain response playbooks for scanner-induced instability and accidental out-of-scope requests.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Maintain response playbooks for scanner-induced instability and accidental out-of-scope requests.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

#### `FWPRO-ERROR-015` — P1 / core
- **هدف کنترل:** Record lessons learned and feed root causes back into secure design and regression tests.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record lessons learned and feed root causes back into secure design and regression tests.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; OWASP_WSTG; NIST_800_61; NIST_CSF; NIST_800_53; ISO27035`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27035](https://www.iso.org/standard/78973.html)

### SDLC — Secure development lifecycle and verification (20 کنترل)

#### `FWPRO-SDLC-001` — P1 / core
- **هدف کنترل:** Define a documented secure development lifecycle that covers requirements, design, implementation, verification, release and operations.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define a documented secure development lifecycle that covers requirements, design, implementation, verification, release and operations.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-002` — P1 / core
- **هدف کنترل:** Train developers and reviewers on relevant vulnerability classes and secure patterns.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Train developers and reviewers on relevant vulnerability classes and secure patterns.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-003` — P1 / core
- **هدف کنترل:** Require peer review and risk-based security review before merging sensitive changes.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Require peer review and risk-based security review before merging sensitive changes.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-004` — P1 / core
- **هدف کنترل:** Use code analysis and secret detection in CI for relevant repositories.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use code analysis and secret detection in CI for relevant repositories.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-005` — P1 / core
- **هدف کنترل:** Run unit, integration, API contract and security regression tests in CI.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Run unit, integration, API contract and security regression tests in CI.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-006` — P1 / core
- **هدف کنترل:** Require tests for vulnerability fixes and security-relevant incident root causes.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Require tests for vulnerability fixes and security-relevant incident root causes.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-007` — P1 / core
- **هدف کنترل:** Establish security acceptance criteria for high-risk features before implementation.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Establish security acceptance criteria for high-risk features before implementation.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-008` — P1 / core
- **هدف کنترل:** Keep security exceptions traceable, time-bound and approved by an accountable owner.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Keep security exceptions traceable, time-bound and approved by an accountable owner.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-009` — P1 / core
- **هدف کنترل:** Run threat modeling for significant design changes and external integrations.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Run threat modeling for significant design changes and external integrations.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-010` — P1 / core
- **هدف کنترل:** Separate build, test and release privileges and restrict CI tokens to least privilege.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Separate build, test and release privileges and restrict CI tokens to least privilege.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-011` — P1 / core
- **هدف کنترل:** Protect build and deployment workflows from untrusted pull-request code execution.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Protect build and deployment workflows from untrusted pull-request code execution.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-012` — P1 / core
- **هدف کنترل:** Pin third-party actions and build dependencies to immutable versions/identifiers where feasible.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Pin third-party actions and build dependencies to immutable versions/identifiers where feasible.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-013` — P1 / core
- **هدف کنترل:** Use isolated, ephemeral and access-limited build agents for release pipelines.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use isolated, ephemeral and access-limited build agents for release pipelines.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-014` — P1 / core
- **هدف کنترل:** Require artifact provenance and integrity verification for production releases where supported.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Require artifact provenance and integrity verification for production releases where supported.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-015` — P1 / core
- **هدف کنترل:** Use reproducible or repeatable build practices when proportionate and technically feasible.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use reproducible or repeatable build practices when proportionate and technically feasible.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-016` — P1 / core
- **هدف کنترل:** Maintain an inventory of source repositories, release branches and maintainers.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Maintain an inventory of source repositories, release branches and maintainers.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-017` — P1 / core
- **هدف کنترل:** Define change approval, emergency change and rollback processes for security-sensitive releases.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define change approval, emergency change and rollback processes for security-sensitive releases.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-018` — P1 / core
- **هدف کنترل:** Perform independent penetration testing for high-risk releases and major architecture changes.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Perform independent penetration testing for high-risk releases and major architecture changes.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-019` — P1 / core
- **هدف کنترل:** Track test coverage by requirements and risk instead of using line coverage as a security-quality proxy.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Track test coverage by requirements and risk instead of using line coverage as a security-quality proxy.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SDLC-020` — P1 / core
- **هدف کنترل:** Measure vulnerability age, recurrence, remediation SLA and exception expiry.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Measure vulnerability age, recurrence, remediation SLA and exception expiry.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_SAMM; OWASP_ASVS; NIST_SSDF; NIST_CSF; ISO27034; ISO27001; CISA_SECURE_BY_DESIGN; OPENSSF_SCORECARD; SLSA; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [SLSA](https://slsa.dev/spec/v1.2/) · [SLSA_PROVENANCE](https://in-toto.io/)

### SUPPLY — Software supply chain, dependencies and artifacts (18 کنترل)

#### `FWPRO-SUPPLY-001` — P1 / core
- **هدف کنترل:** Maintain a resolved dependency inventory including transitive dependencies for each release artifact.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Maintain a resolved dependency inventory including transitive dependencies for each release artifact.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-002` — P1 / core
- **هدف کنترل:** Generate a valid SBOM in an agreed format such as CycloneDX or SPDX from the resolved build output.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Generate a valid SBOM in an agreed format such as CycloneDX or SPDX from the resolved build output.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-003` — P1 / core
- **هدف کنترل:** Scan direct and transitive dependencies for known vulnerabilities and record database freshness.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Scan direct and transitive dependencies for known vulnerabilities and record database freshness.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-004` — P1 / core
- **هدف کنترل:** Map vulnerable components to exact package versions and deployed artifacts before assigning exposure.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Map vulnerable components to exact package versions and deployed artifacts before assigning exposure.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-005` — P1 / core
- **هدف کنترل:** Prioritize known-exploited CVEs using verified CISA KEV matches and contextual risk.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Prioritize known-exploited CVEs using verified CISA KEV matches and contextual risk.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-006` — P1 / core
- **هدف کنترل:** Use EPSS only as an exploit-likelihood input for known CVEs and preserve source timestamp.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use EPSS only as an exploit-likelihood input for known CVEs and preserve source timestamp.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-007` — P1 / core
- **هدف کنترل:** Pin dependencies and review updates to reduce unreviewed drift and dependency confusion.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Pin dependencies and review updates to reduce unreviewed drift and dependency confusion.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-008` — P1 / core
- **هدف کنترل:** Verify package provenance/signatures where ecosystems provide reliable mechanisms.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Verify package provenance/signatures where ecosystems provide reliable mechanisms.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-009` — P1 / core
- **هدف کنترل:** Use private registry namespace controls and prevent dependency confusion.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use private registry namespace controls and prevent dependency confusion.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-010` — P1 / core
- **هدف کنترل:** Review package maintainership, update activity and unexpected install/build scripts for high-risk components.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Review package maintainership, update activity and unexpected install/build scripts for high-risk components.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-011` — P1 / core
- **هدف کنترل:** Remove unused and abandoned dependencies from release artifacts.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Remove unused and abandoned dependencies from release artifacts.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-012` — P1 / core
- **هدف کنترل:** Produce provenance linking source revision, workflow, builder, dependencies and output artifact.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Produce provenance linking source revision, workflow, builder, dependencies and output artifact.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-013` — P1 / core
- **هدف کنترل:** Protect release signing keys and separate signing permissions from ordinary CI jobs.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Protect release signing keys and separate signing permissions from ordinary CI jobs.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-014` — P1 / core
- **هدف کنترل:** Prevent secrets, test fixtures and local databases from entering source packages and release archives.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Prevent secrets, test fixtures and local databases from entering source packages and release archives.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-015` — P1 / core
- **هدف کنترل:** Scan container images and generated artifacts, not only source manifests.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Scan container images and generated artifacts, not only source manifests.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-016` — P1 / core
- **هدف کنترل:** Track license obligations and component attribution in accordance with organizational policy.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Track license obligations and component attribution in accordance with organizational policy.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-017` — P1 / core
- **هدف کنترل:** Define a vulnerability response policy for dependency advisories and upstream maintainer disclosures.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Define a vulnerability response policy for dependency advisories and upstream maintainer disclosures.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-SUPPLY-018` — P1 / core
- **هدف کنترل:** Record dependency scanner/tool version, database timestamp and triage decision for each release.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Record dependency scanner/tool version, database timestamp and triage decision for each release.
- **شواهد مورد انتظار:** Tool name/version, database freshness, machine-readable output and triage record.
- **روش راستی‌آزمایی:** `external_tool`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_TOP10; OWASP_ASVS; NIST_SSDF; CIS_CONTROLS; CYCLONEDX; SPDX; SLSA; OPENSSF_SCORECARD; CWE_TOP25; SLSA_PROVENANCE`
- **منابع رسمی:** [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CYCLONEDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/specifications/) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [SLSA_PROVENANCE](https://in-toto.io/)

### CLOUD — Cloud, container, Kubernetes and infrastructure as code (18 کنترل)

#### `FWPRO-CLOUD-001` — P1 / conditional
- **هدف کنترل:** Define shared-responsibility boundaries for each cloud service, managed platform and third-party provider.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Define shared-responsibility boundaries for each cloud service, managed platform and third-party provider.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-002` — P1 / conditional
- **هدف کنترل:** Restrict cloud IAM roles, service accounts and workload identities to required actions/resources.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Restrict cloud IAM roles, service accounts and workload identities to required actions/resources.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-003` — P1 / conditional
- **هدف کنترل:** Prevent public access to storage, databases, snapshots and administrative services unless explicitly justified.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Prevent public access to storage, databases, snapshots and administrative services unless explicitly justified.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-004` — P1 / conditional
- **هدف کنترل:** Store secrets in a managed secret service and avoid baking them into images or IaC state.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Store secrets in a managed secret service and avoid baking them into images or IaC state.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-005` — P1 / conditional
- **هدف کنترل:** Scan IaC for public exposure, overly broad IAM, weak encryption and unsafe network rules.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Scan IaC for public exposure, overly broad IAM, weak encryption and unsafe network rules.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-006` — P1 / conditional
- **هدف کنترل:** Build containers from maintained minimal base images and rebuild when critical updates apply.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Build containers from maintained minimal base images and rebuild when critical updates apply.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-007` — P1 / conditional
- **هدف کنترل:** Run containers as non-root where feasible and remove unnecessary capabilities.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Run containers as non-root where feasible and remove unnecessary capabilities.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-008` — P1 / conditional
- **هدف کنترل:** Use read-only filesystems, resource limits and seccomp/AppArmor or platform-equivalent controls where appropriate.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use read-only filesystems, resource limits and seccomp/AppArmor or platform-equivalent controls where appropriate.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-009` — P1 / conditional
- **هدف کنترل:** Pin container images by immutable digest for production deployments where feasible.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Pin container images by immutable digest for production deployments where feasible.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-010` — P1 / conditional
- **هدف کنترل:** Restrict Kubernetes API access, RBAC, admission policy and exposed dashboards.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Restrict Kubernetes API access, RBAC, admission policy and exposed dashboards.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-011` — P1 / conditional
- **هدف کنترل:** Avoid privileged pods, host-path mounts and broad host namespace access unless explicitly approved.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Avoid privileged pods, host-path mounts and broad host namespace access unless explicitly approved.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-012` — P1 / conditional
- **هدف کنترل:** Separate workloads and secrets across environments and trust zones.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Separate workloads and secrets across environments and trust zones.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-013` — P1 / conditional
- **هدف کنترل:** Apply egress controls for workloads that can fetch arbitrary URLs or contact external services.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Apply egress controls for workloads that can fetch arbitrary URLs or contact external services.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-014` — P1 / conditional
- **هدف کنترل:** Review cloud audit logging, key management, backup protection and configuration drift.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Review cloud audit logging, key management, backup protection and configuration drift.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-015` — P1 / conditional
- **هدف کنترل:** Use the exact CIS Benchmark release for the product and version being assessed.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use the exact CIS Benchmark release for the product and version being assessed.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-016` — P1 / conditional
- **هدف کنترل:** Protect Terraform/CloudFormation state and CI plan output from secrets disclosure.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Protect Terraform/CloudFormation state and CI plan output from secrets disclosure.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-017` — P1 / conditional
- **هدف کنترل:** Require review and approval for infrastructure changes affecting internet exposure or access boundaries.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Require review and approval for infrastructure changes affecting internet exposure or access boundaries.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

#### `FWPRO-CLOUD-018` — P1 / conditional
- **هدف کنترل:** Test restore and failover for critical cloud resources and managed data services.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Test restore and failover for critical cloud resources and managed data services.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `OWASP_CLOUD_NATIVE; NIST_800_53; NIST_CSF; ISO27017; CIS_CONTROLS; CIS_BENCHMARKS; SLSA`
- **منابع رسمی:** [OWASP_CLOUD_NATIVE](https://owasp.org/projects/cloud-native-application-security-top-10) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27017](https://www.iso.org/standard/27017) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [CIS_BENCHMARKS](https://www.cisecurity.org/cis-benchmarks) · [SLSA](https://slsa.dev/spec/v1.2/)

### AVAIL — Availability, resilience, rate limiting and recovery (15 کنترل)

#### `FWPRO-AVAIL-001` — P1 / core
- **هدف کنترل:** Set explicit request, body, upload, response and processing timeouts throughout the stack.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Set explicit request, body, upload, response and processing timeouts throughout the stack.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-002` — P1 / core
- **هدف کنترل:** Limit concurrency, queue length and per-tenant work to prevent resource starvation.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Limit concurrency, queue length and per-tenant work to prevent resource starvation.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-003` — P1 / core
- **هدف کنترل:** Apply rate limiting consistently across login, search, exports, API and expensive business paths.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Apply rate limiting consistently across login, search, exports, API and expensive business paths.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-004` — P1 / core
- **هدف کنترل:** Bound regular-expression, decompression, image/document and GraphQL query processing costs.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Bound regular-expression, decompression, image/document and GraphQL query processing costs.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-005` — P1 / core
- **هدف کنترل:** Define service-level objectives, availability targets and business impact of downtime.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define service-level objectives, availability targets and business impact of downtime.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-006` — P1 / core
- **هدف کنترل:** Maintain tested backups with access separation, retention and recovery objectives.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Maintain tested backups with access separation, retention and recovery objectives.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-007` — P1 / core
- **هدف کنترل:** Exercise restore and disaster-recovery procedures and record achieved recovery time/data loss.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Exercise restore and disaster-recovery procedures and record achieved recovery time/data loss.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-008` — P1 / core
- **هدف کنترل:** Test safe degradation when identity, payment, messaging, database or third-party services are unavailable.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test safe degradation when identity, payment, messaging, database or third-party services are unavailable.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-009` — P1 / core
- **هدف کنترل:** Use circuit breakers/retry budgets and avoid unbounded retries across dependencies.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use circuit breakers/retry budgets and avoid unbounded retries across dependencies.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-010` — P1 / core
- **هدف کنترل:** Protect queues and scheduled work against unbounded growth, poison messages and repeated execution.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Protect queues and scheduled work against unbounded growth, poison messages and repeated execution.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-011` — P1 / core
- **هدف کنترل:** Assess availability risks from slow client reads, large responses and connection exhaustion.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Assess availability risks from slow client reads, large responses and connection exhaustion.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-012` — P1 / core
- **هدف کنترل:** Perform load/stress/DoS tests only with explicit authorization and an agreed safe environment/window.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Perform load/stress/DoS tests only with explicit authorization and an agreed safe environment/window.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-013` — P1 / core
- **هدف کنترل:** Define operational thresholds and automatic stop rules for scans that increase target errors or latency.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define operational thresholds and automatic stop rules for scans that increase target errors or latency.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-014` — P1 / core
- **هدف کنترل:** Maintain rollback plans for deployment failures and security hotfixes.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Maintain rollback plans for deployment failures and security hotfixes.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

#### `FWPRO-AVAIL-015` — P1 / core
- **هدف کنترل:** Review multi-region/zone recovery and dependency single points of failure when the service needs them.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Review multi-region/zone recovery and dependency single points of failure when the service needs them.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_API; OWASP_ATWA; NIST_CSF; NIST_800_53; ISO27001; ISO31000; NIST_800_61`
- **منابع رسمی:** [OWASP_API](https://owasp.org/www-project-api-security/) · [OWASP_ATWA](https://owasp.org/www-project-automated-threats-to-web-applications/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO31000](https://www.iso.org/standard/65694.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

### VULN — Vulnerability management, disclosure and remediation (15 کنترل)

#### `FWPRO-VULN-001` — P1 / core
- **هدف کنترل:** Maintain a published vulnerability reporting channel and a clear product security contact.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Maintain a published vulnerability reporting channel and a clear product security contact.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-002` — P1 / core
- **هدف کنترل:** Define intake, acknowledgment, triage, reproduction, assignment, disclosure and closure workflows.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define intake, acknowledgment, triage, reproduction, assignment, disclosure and closure workflows.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-003` — P1 / core
- **هدف کنترل:** Assign unique finding IDs and preserve source scan, affected asset, evidence and remediation history.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Assign unique finding IDs and preserve source scan, affected asset, evidence and remediation history.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-004` — P1 / core
- **هدف کنترل:** Use CVSS v4.0 only when metrics and vector are defensibly assessed; keep heuristic risk separate.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use CVSS v4.0 only when metrics and vector are defensibly assessed; keep heuristic risk separate.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-005` — P1 / core
- **هدف کنترل:** Track confidence separately from impact/severity and require human verification for high-impact candidates.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Track confidence separately from impact/severity and require human verification for high-impact candidates.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-006` — P1 / core
- **هدف کنترل:** Check KEV and EPSS data freshness when prioritizing known CVEs; record match rationale.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Check KEV and EPSS data freshness when prioritizing known CVEs; record match rationale.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-007` — P1 / core
- **هدف کنترل:** Set remediation SLAs by severity, exposure, exploitability and business context.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Set remediation SLAs by severity, exposure, exploitability and business context.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-008` — P1 / core
- **هدف کنترل:** Require regression tests and retesting after fixes, with state transitions recorded.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Require regression tests and retesting after fixes, with state transitions recorded.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-009` — P1 / core
- **هدف کنترل:** Provide a documented false-positive process with rationale, reviewer and expiry/review date.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Provide a documented false-positive process with rationale, reviewer and expiry/review date.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-010` — P1 / core
- **هدف کنترل:** Require formal risk acceptance with compensating controls and an expiration date.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Require formal risk acceptance with compensating controls and an expiration date.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-011` — P1 / core
- **هدف کنترل:** Coordinate disclosure with affected customers, maintainers and downstream users as appropriate.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Coordinate disclosure with affected customers, maintainers and downstream users as appropriate.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-012` — P1 / core
- **هدف کنترل:** Preserve sanitized evidence without collecting more sensitive data than necessary.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Preserve sanitized evidence without collecting more sensitive data than necessary.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-013` — P1 / core
- **هدف کنترل:** Track repeated/root-cause vulnerabilities and update design guidance or shared libraries.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Track repeated/root-cause vulnerabilities and update design guidance or shared libraries.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-014` — P1 / core
- **هدف کنترل:** Define a process for emergency mitigations when complete remediation is not immediately possible.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define a process for emergency mitigations when complete remediation is not immediately possible.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

#### `FWPRO-VULN-015` — P1 / core
- **هدف کنترل:** Provide customers with actionable advisories and upgrade/remediation guidance when disclosure is appropriate.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Provide customers with actionable advisories and upgrade/remediation guidance when disclosure is appropriate.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; NIST_CSF; OWASP_SAMM; OWASP_ASVS; CWE_TOP25; CVSS; EPSS; CISA_KEV`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [OWASP_SAMM](https://owaspsamm.org/model/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) · [CVSS](https://www.first.org/cvss/v4.0/) · [EPSS](https://www.first.org/epss/) · [CISA_KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

### PRIVREG — Privacy, legal and sectoral applicability review (12 کنترل)

#### `FWPRO-PRIVREG-001` — P1 / conditional
- **هدف کنترل:** Record which jurisdictions, sectors, contracts and data types make regulatory checklists applicable.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record which jurisdictions, sectors, contracts and data types make regulatory checklists applicable.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-002` — P1 / conditional
- **هدف کنترل:** Document controller/processor roles and data-processing terms where GDPR or equivalent privacy law applies.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document controller/processor roles and data-processing terms where GDPR or equivalent privacy law applies.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-003` — P1 / conditional
- **هدف کنترل:** Assess whether a data protection impact assessment is required for the processing context.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Assess whether a data protection impact assessment is required for the processing context.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-004` — P1 / conditional
- **هدف کنترل:** Map personal-data incident workflows to notification duties and applicable timelines through legal review.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Map personal-data incident workflows to notification duties and applicable timelines through legal review.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-005` — P1 / conditional
- **هدف کنترل:** For PCI DSS scope, document cardholder-data flows, connected systems and segmentation evidence.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: For PCI DSS scope, document cardholder-data flows, connected systems and segmentation evidence.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-006` — P1 / conditional
- **هدف کنترل:** For PCI DSS engagements, use required approved scanning/testing methods and qualified assessors where applicable.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: For PCI DSS engagements, use required approved scanning/testing methods and qualified assessors where applicable.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-007` — P1 / conditional
- **هدف کنترل:** For HIPAA scope, maintain risk analysis, access controls, audit controls and contingency evidence for ePHI.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: For HIPAA scope, maintain risk analysis, access controls, audit controls and contingency evidence for ePHI.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-008` — P1 / conditional
- **هدف کنترل:** For SOC 2, map controls to the applicable current AICPA Trust Services Criteria with the auditor.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: For SOC 2, map controls to the applicable current AICPA Trust Services Criteria with the auditor.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-009` — P1 / conditional
- **هدف کنترل:** For NIS2/DORA scope, verify entity classification, national law, sector rules and reporting obligations with counsel.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: For NIS2/DORA scope, verify entity classification, national law, sector rules and reporting obligations with counsel.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-010` — P1 / conditional
- **هدف کنترل:** For cloud contracts, document shared responsibilities, subprocessors, regions and audit/evidence rights.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: For cloud contracts, document shared responsibilities, subprocessors, regions and audit/evidence rights.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-011` — P1 / conditional
- **هدف کنترل:** Do not claim GDPR, PCI, SOC 2, HIPAA, NIS2, DORA or ISO certification from scanner results alone.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Do not claim GDPR, PCI, SOC 2, HIPAA, NIS2, DORA or ISO certification from scanner results alone.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-PRIVREG-012` — P1 / conditional
- **هدف کنترل:** Keep legal interpretations, applicability determinations and compliance sign-off owned by qualified personnel.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Keep legal interpretations, applicability determinations and compliance sign-off owned by qualified personnel.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `GDPR; NIS2; DORA; PCI_DSS; HIPAA; SOC2; ISO27701; NIST_PRIVACY; NIST_800_53`
- **منابع رسمی:** [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [PCI_DSS](https://www.pcisecuritystandards.org/document_library/) · [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [SOC2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) · [ISO27701](https://www.iso.org/standard/27701) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

### ACCESS — Accessibility and inclusive product interface (12 کنترل)

#### `FWPRO-ACCESS-001` — P2 / adjacent
- **هدف کنترل:** Provide keyboard access to all interactive controls without keyboard traps.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Provide keyboard access to all interactive controls without keyboard traps.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-002` — P2 / adjacent
- **هدف کنترل:** Maintain visible focus indicators and logical focus order.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Maintain visible focus indicators and logical focus order.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-003` — P2 / adjacent
- **هدف کنترل:** Associate form labels, descriptions and error messages programmatically with controls.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Associate form labels, descriptions and error messages programmatically with controls.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-004` — P2 / adjacent
- **هدف کنترل:** Provide sufficient text and non-text contrast under the target WCAG conformance level.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Provide sufficient text and non-text contrast under the target WCAG conformance level.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-005` — P2 / adjacent
- **هدف کنترل:** Expose dynamic scan state, validation errors and status messages to assistive technologies.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Expose dynamic scan state, validation errors and status messages to assistive technologies.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-006` — P2 / adjacent
- **هدف کنترل:** Avoid relying on color alone to convey severity, status or error state.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Avoid relying on color alone to convey severity, status or error state.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-007` — P2 / adjacent
- **هدف کنترل:** Support zoom/reflow and responsive layouts without loss of critical functionality.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Support zoom/reflow and responsive layouts without loss of critical functionality.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-008` — P2 / adjacent
- **هدف کنترل:** Provide meaningful accessible names for icon-only controls and report download actions.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Provide meaningful accessible names for icon-only controls and report download actions.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-009` — P2 / adjacent
- **هدف کنترل:** Check focus movement and modal/dialog behavior in keyboard and screen-reader tests.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Check focus movement and modal/dialog behavior in keyboard and screen-reader tests.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-010` — P2 / adjacent
- **هدف کنترل:** Include automated accessibility checks plus manual assistive-technology verification for applicable criteria.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Include automated accessibility checks plus manual assistive-technology verification for applicable criteria.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-011` — P2 / adjacent
- **هدف کنترل:** Record target conformance level and applicable legal/procurement standard before declaring accessibility status.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Record target conformance level and applicable legal/procurement standard before declaring accessibility status.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

#### `FWPRO-ACCESS-012` — P2 / adjacent
- **هدف کنترل:** Test language metadata, page title, headings and table header associations.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Test language metadata, page title, headings and table header associations.
- **شواهد مورد انتظار:** Automated scan result plus manual keyboard/screen-reader verification evidence.
- **روش راستی‌آزمایی:** `automated_plus_manual`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; NIST_CSF`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [NIST_CSF](https://www.nist.gov/cyberframework)

### MOBILE — Mobile application security (conditional) (10 کنترل)

#### `FWPRO-MOBILE-001` — P2 / conditional
- **هدف کنترل:** Inventory mobile app identifiers, signing keys, supported platform versions and release channels.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Inventory mobile app identifiers, signing keys, supported platform versions and release channels.
- **شواهد مورد انتظار:** Specialist tool/test record, device/environment details, sanitized evidence and assessor review.
- **روش راستی‌آزمایی:** `specialist_tool`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_MASVS; OWASP_MASTG; OWASP_ASVS; OWASP_CHEATSHEETS`
- **منابع رسمی:** [OWASP_MASVS](https://mas.owasp.org/MASVS/) · [OWASP_MASTG](https://mas.owasp.org/MASTG/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/)

#### `FWPRO-MOBILE-002` — P2 / conditional
- **هدف کنترل:** Avoid storing long-lived secrets or sensitive records in insecure device storage.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Avoid storing long-lived secrets or sensitive records in insecure device storage.
- **شواهد مورد انتظار:** Specialist tool/test record, device/environment details, sanitized evidence and assessor review.
- **روش راستی‌آزمایی:** `specialist_tool`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_MASVS; OWASP_MASTG; OWASP_ASVS; OWASP_CHEATSHEETS`
- **منابع رسمی:** [OWASP_MASVS](https://mas.owasp.org/MASVS/) · [OWASP_MASTG](https://mas.owasp.org/MASTG/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/)

#### `FWPRO-MOBILE-003` — P2 / conditional
- **هدف کنترل:** Use platform-backed key storage and modern cryptographic APIs for sensitive mobile data.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use platform-backed key storage and modern cryptographic APIs for sensitive mobile data.
- **شواهد مورد انتظار:** Specialist tool/test record, device/environment details, sanitized evidence and assessor review.
- **روش راستی‌آزمایی:** `specialist_tool`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_MASVS; OWASP_MASTG; OWASP_ASVS; OWASP_CHEATSHEETS`
- **منابع رسمی:** [OWASP_MASVS](https://mas.owasp.org/MASVS/) · [OWASP_MASTG](https://mas.owasp.org/MASTG/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/)

#### `FWPRO-MOBILE-004` — P2 / conditional
- **هدف کنترل:** Validate TLS and certificate behavior, including unsafe trust overrides and debug-only network settings.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Validate TLS and certificate behavior, including unsafe trust overrides and debug-only network settings.
- **شواهد مورد انتظار:** Specialist tool/test record, device/environment details, sanitized evidence and assessor review.
- **روش راستی‌آزمایی:** `specialist_tool`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_MASVS; OWASP_MASTG; OWASP_ASVS; OWASP_CHEATSHEETS`
- **منابع رسمی:** [OWASP_MASVS](https://mas.owasp.org/MASVS/) · [OWASP_MASTG](https://mas.owasp.org/MASTG/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/)

#### `FWPRO-MOBILE-005` — P2 / conditional
- **هدف کنترل:** Protect deep links, app links, intent handlers and inter-app messages against unauthorized actions.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Protect deep links, app links, intent handlers and inter-app messages against unauthorized actions.
- **شواهد مورد انتظار:** Specialist tool/test record, device/environment details, sanitized evidence and assessor review.
- **روش راستی‌آزمایی:** `specialist_tool`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_MASVS; OWASP_MASTG; OWASP_ASVS; OWASP_CHEATSHEETS`
- **منابع رسمی:** [OWASP_MASVS](https://mas.owasp.org/MASVS/) · [OWASP_MASTG](https://mas.owasp.org/MASTG/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/)

#### `FWPRO-MOBILE-006` — P2 / conditional
- **هدف کنترل:** Review exported Android components, entitlements, URL schemes and platform permissions.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Review exported Android components, entitlements, URL schemes and platform permissions.
- **شواهد مورد انتظار:** Specialist tool/test record, device/environment details, sanitized evidence and assessor review.
- **روش راستی‌آزمایی:** `specialist_tool`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_MASVS; OWASP_MASTG; OWASP_ASVS; OWASP_CHEATSHEETS`
- **منابع رسمی:** [OWASP_MASVS](https://mas.owasp.org/MASVS/) · [OWASP_MASTG](https://mas.owasp.org/MASTG/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/)

#### `FWPRO-MOBILE-007` — P2 / conditional
- **هدف کنترل:** Prevent sensitive data from leaking through logs, screenshots, clipboard, backups or notifications where relevant.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Prevent sensitive data from leaking through logs, screenshots, clipboard, backups or notifications where relevant.
- **شواهد مورد انتظار:** Specialist tool/test record, device/environment details, sanitized evidence and assessor review.
- **روش راستی‌آزمایی:** `specialist_tool`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_MASVS; OWASP_MASTG; OWASP_ASVS; OWASP_CHEATSHEETS`
- **منابع رسمی:** [OWASP_MASVS](https://mas.owasp.org/MASVS/) · [OWASP_MASTG](https://mas.owasp.org/MASTG/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/)

#### `FWPRO-MOBILE-008` — P2 / conditional
- **هدف کنترل:** Review root/jailbreak, tampering and reverse-engineering mitigations according to actual risk.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Review root/jailbreak, tampering and reverse-engineering mitigations according to actual risk.
- **شواهد مورد انتظار:** Specialist tool/test record, device/environment details, sanitized evidence and assessor review.
- **روش راستی‌آزمایی:** `specialist_tool`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_MASVS; OWASP_MASTG; OWASP_ASVS; OWASP_CHEATSHEETS`
- **منابع رسمی:** [OWASP_MASVS](https://mas.owasp.org/MASVS/) · [OWASP_MASTG](https://mas.owasp.org/MASTG/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/)

#### `FWPRO-MOBILE-009` — P2 / conditional
- **هدف کنترل:** Use MASVS and MASTG test cases for each supported platform and record device/OS/tool versions.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use MASVS and MASTG test cases for each supported platform and record device/OS/tool versions.
- **شواهد مورد انتظار:** Specialist tool/test record, device/environment details, sanitized evidence and assessor review.
- **روش راستی‌آزمایی:** `specialist_tool`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_MASVS; OWASP_MASTG; OWASP_ASVS; OWASP_CHEATSHEETS`
- **منابع رسمی:** [OWASP_MASVS](https://mas.owasp.org/MASVS/) · [OWASP_MASTG](https://mas.owasp.org/MASTG/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/)

#### `FWPRO-MOBILE-010` — P2 / conditional
- **هدف کنترل:** Treat a web/API scan as complementary; do not claim mobile MASVS conformance without mobile testing.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Treat a web/API scan as complementary; do not claim mobile MASVS conformance without mobile testing.
- **شواهد مورد انتظار:** Specialist tool/test record, device/environment details, sanitized evidence and assessor review.
- **روش راستی‌آزمایی:** `specialist_tool`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `OWASP_MASVS; OWASP_MASTG; OWASP_ASVS; OWASP_CHEATSHEETS`
- **منابع رسمی:** [OWASP_MASVS](https://mas.owasp.org/MASVS/) · [OWASP_MASTG](https://mas.owasp.org/MASTG/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_CHEATSHEETS](https://cheatsheetseries.owasp.org/)

### AI — AI/LLM/agent security (conditional) (14 کنترل)

#### `FWPRO-AI-001` — P1 / conditional
- **هدف کنترل:** Inventory models, model versions, providers, prompts, tools, retrieval sources and sensitive data paths.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Inventory models, model versions, providers, prompts, tools, retrieval sources and sensitive data paths.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-002` — P1 / conditional
- **هدف کنترل:** Test direct and indirect prompt-injection resistance using approved, non-destructive test fixtures.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Test direct and indirect prompt-injection resistance using approved, non-destructive test fixtures.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-003` — P1 / conditional
- **هدف کنترل:** Prevent untrusted retrieved content from gaining system-level authority or bypassing policy constraints.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Prevent untrusted retrieved content from gaining system-level authority or bypassing policy constraints.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-004` — P1 / conditional
- **هدف کنترل:** Apply least privilege and per-tool authorization to agent actions; require approval for high-impact actions.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Apply least privilege and per-tool authorization to agent actions; require approval for high-impact actions.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-005` — P1 / conditional
- **هدف کنترل:** Validate and constrain model outputs before SQL, shell, HTML, code, URL or API execution.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Validate and constrain model outputs before SQL, shell, HTML, code, URL or API execution.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-006` — P1 / conditional
- **هدف کنترل:** Limit token use, tool calls, recursion, response size and external-call spend to prevent resource abuse.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Limit token use, tool calls, recursion, response size and external-call spend to prevent resource abuse.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-007` — P1 / conditional
- **هدف کنترل:** Prevent model prompts, hidden system instructions, credentials and private retrieval context from being disclosed.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Prevent model prompts, hidden system instructions, credentials and private retrieval context from being disclosed.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-008` — P1 / conditional
- **هدف کنترل:** Isolate tenants and enforce authorization at retrieval time, not only in prompt instructions.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Isolate tenants and enforce authorization at retrieval time, not only in prompt instructions.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-009` — P1 / conditional
- **هدف کنترل:** Validate data provenance and access controls for embeddings, vector stores, training and fine-tuning data.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Validate data provenance and access controls for embeddings, vector stores, training and fine-tuning data.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-010` — P1 / conditional
- **هدف کنترل:** Evaluate model supply-chain risk, plugins/tools, external data and model licensing/provenance.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Evaluate model supply-chain risk, plugins/tools, external data and model licensing/provenance.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-011` — P1 / conditional
- **هدف کنترل:** Log model/tool actions with redaction and reconstructable trace IDs without retaining unnecessary private content.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Log model/tool actions with redaction and reconstructable trace IDs without retaining unnecessary private content.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-012` — P1 / conditional
- **هدف کنترل:** Perform human review and incident handling for high-impact AI outputs and automated decisions.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Perform human review and incident handling for high-impact AI outputs and automated decisions.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-013` — P1 / conditional
- **هدف کنترل:** Document known limitations, evaluation datasets, misuse tests, acceptance thresholds and rollback criteria.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Document known limitations, evaluation datasets, misuse tests, acceptance thresholds and rollback criteria.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

#### `FWPRO-AI-014` — P1 / conditional
- **هدف کنترل:** Do not treat generic prompt safety filters as proof that prompt injection or data exfiltration is impossible.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Do not treat generic prompt safety filters as proof that prompt injection or data exfiltration is impossible.
- **شواهد مورد انتظار:** Reproducible test case, approved test account/environment, tool/version and reviewer validation.
- **روش راستی‌آزمایی:** `manual_or_specialist_tool`
- **نوع رابطه با مراجع:** conditional, supporting
- **مراجع مرتبط:** `OWASP_LLM; NIST_AI_RMF; NIST_AI_GENAI; ISO42001; NIST_PRIVACY`
- **منابع رسمی:** [OWASP_LLM](https://genai.owasp.org/llm-top-10/) · [NIST_AI_RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST_AI_GENAI](https://www.nist.gov/itl/ai-risk-management-framework) · [ISO42001](https://www.iso.org/standard/81230.html) · [NIST_PRIVACY](https://www.nist.gov/privacy-framework)

### SCANNER — Security testing product / scanner assurance (20 کنترل)

#### `FWPRO-SCANNER-001` — P0 / core
- **هدف کنترل:** Require a fail-closed target scope check before every network request and follow-up operation.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Require a fail-closed target scope check before every network request and follow-up operation.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-002` — P0 / core
- **هدف کنترل:** Revalidate scope after redirects, DNS resolution changes and browser-generated requests.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Revalidate scope after redirects, DNS resolution changes and browser-generated requests.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-003` — P0 / core
- **هدف کنترل:** Never forward credentials across scheme/host/port origins without an explicit separate credential profile.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Never forward credentials across scheme/host/port origins without an explicit separate credential profile.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-004` — P0 / core
- **هدف کنترل:** Enforce per-job rate, concurrency, page, depth, endpoint, byte and time budgets.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Enforce per-job rate, concurrency, page, depth, endpoint, byte and time budgets.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-005` — P0 / core
- **هدف کنترل:** Provide cancellation checkpoints and ensure canceled scans stop issuing new requests promptly.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Provide cancellation checkpoints and ensure canceled scans stop issuing new requests promptly.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-006` — P0 / core
- **هدف کنترل:** Redact tokens, passwords, session IDs and secret-like data before database/log/report persistence.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Redact tokens, passwords, session IDs and secret-like data before database/log/report persistence.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-007` — P0 / core
- **هدف کنترل:** Do not execute arbitrary shell commands or code generated by an LLM or remote target content.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Do not execute arbitrary shell commands or code generated by an LLM or remote target content.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-008` — P0 / core
- **هدف کنترل:** Treat target HTML, JS, headers and API specifications as untrusted input and prevent prompt/code injection into tooling.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Treat target HTML, JS, headers and API specifications as untrusted input and prevent prompt/code injection into tooling.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-009` — P0 / core
- **هدف کنترل:** Keep optional ZAP or specialist-tool adapters disabled by default and scope their URLs independently.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Keep optional ZAP or specialist-tool adapters disabled by default and scope their URLs independently.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-010` — P0 / core
- **هدف کنترل:** Use a dedicated isolated test target for E2E tests; do not point automated tests at public targets.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use a dedicated isolated test target for E2E tests; do not point automated tests at public targets.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-011` — P0 / core
- **هدف کنترل:** Test HTTP client behavior for redirect, DNS/IP policy, TLS errors, decompression limits and malformed responses.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Test HTTP client behavior for redirect, DNS/IP policy, TLS errors, decompression limits and malformed responses.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-012` — P0 / core
- **هدف کنترل:** Store scan configuration and result provenance without storing raw credentials.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Store scan configuration and result provenance without storing raw credentials.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-013` — P0 / core
- **هدف کنترل:** Ensure report bundles contain only files for that scan and verify path/size/hash consistency.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Ensure report bundles contain only files for that scan and verify path/size/hash consistency.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-014` — P0 / core
- **هدف کنترل:** Use a stable documented finding schema with rule IDs, confidence, severity, evidence, remediation and references.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use a stable documented finding schema with rule IDs, confidence, severity, evidence, remediation and references.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-015` — P0 / core
- **هدف کنترل:** Distinguish no finding, not tested, not applicable, blocked and manually required states.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Distinguish no finding, not tested, not applicable, blocked and manually required states.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-016` — P0 / core
- **هدف کنترل:** Track scanner version, rule-set version, dependency inventory and start/end timestamps in each report.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Track scanner version, rule-set version, dependency inventory and start/end timestamps in each report.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-017` — P0 / core
- **هدف کنترل:** Run static analysis, dependency audit, secret scanning and container scanning in release CI.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Run static analysis, dependency audit, secret scanning and container scanning in release CI.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-018` — P0 / core
- **هدف کنترل:** Document the scanner’s false-positive/false-negative limitations and do not claim complete vulnerability detection.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Document the scanner’s false-positive/false-negative limitations and do not claim complete vulnerability detection.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-019` — P0 / core
- **هدف کنترل:** Require independent review of new rules that can produce outbound requests or inspect sensitive content.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Require independent review of new rules that can produce outbound requests or inspect sensitive content.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

#### `FWPRO-SCANNER-020` — P0 / core
- **هدف کنترل:** Ensure dashboard output escapes target-derived data and uses safe DOM rendering practices.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Ensure dashboard output escapes target-derived data and uses safe DOM rendering practices.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; NIST_800_115; NIST_SSDF; ISO27034; ISO27001; ISO30111; CVSS; SARIF`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [ISO27034](https://www.iso.org/standard/44378.html) · [ISO27001](https://www.iso.org/standard/27001) · [ISO30111](https://www.iso.org/standard/69725.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html)

### EVIDENCE — Evidence integrity, reporting and audit trail (12 کنترل)

#### `FWPRO-EVIDENCE-001` — P1 / core
- **هدف کنترل:** Every finding identifies the test/rule version, target asset, observation time and verification mode.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Every finding identifies the test/rule version, target asset, observation time and verification mode.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-002` — P1 / core
- **هدف کنترل:** Store minimum necessary sanitized evidence and redact secrets before persistence.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Store minimum necessary sanitized evidence and redact secrets before persistence.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-003` — P1 / core
- **هدف کنترل:** Distinguish observed fact, hypothesis, inference and manually verified conclusion in reports.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Distinguish observed fact, hypothesis, inference and manually verified conclusion in reports.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-004` — P1 / core
- **هدف کنترل:** Include expected behavior, observed behavior, impact, remediation and retest guidance.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Include expected behavior, observed behavior, impact, remediation and retest guidance.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-005` — P1 / core
- **هدف کنترل:** Include coverage and untested limitations in every assessment summary.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Include coverage and untested limitations in every assessment summary.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-006` — P1 / core
- **هدف کنترل:** Provide JSON schema/versioning and validate emitted report formats in CI.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Provide JSON schema/versioning and validate emitted report formats in CI.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-007` — P1 / core
- **هدف کنترل:** Escape HTML/Markdown and neutralize CSV formula injection in export paths.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Escape HTML/Markdown and neutralize CSV formula injection in export paths.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-008` — P1 / core
- **هدف کنترل:** Validate SARIF output with schema and preserve correct rule metadata and result locations.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Validate SARIF output with schema and preserve correct rule metadata and result locations.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-009` — P1 / core
- **هدف کنترل:** Include SHA-256 manifest entries for report bundles and clearly label unsigned manifests.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Include SHA-256 manifest entries for report bundles and clearly label unsigned manifests.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-010` — P1 / core
- **هدف کنترل:** Protect reports using access control, transport security, retention limits and auditable download events.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Protect reports using access control, transport security, retention limits and auditable download events.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-011` — P1 / core
- **هدف کنترل:** Maintain an audit trail for finding state changes and standards-checklist decisions.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Maintain an audit trail for finding state changes and standards-checklist decisions.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

#### `FWPRO-EVIDENCE-012` — P1 / core
- **هدف کنترل:** Require reviewer/approver details and rationale for high-severity closure or risk acceptance.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Require reviewer/approver details and rationale for high-severity closure or risk acceptance.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_WSTG; NIST_800_115; NIST_800_53; ISO27001; SARIF; CVSS; ISO29147; ISO30111`
- **منابع رسمی:** [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [NIST_800_115](https://csrc.nist.gov/pubs/sp/800/115/final) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html) · [CVSS](https://www.first.org/cvss/v4.0/) · [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html)

### STANDARDS — Standards mapping and conformity governance (12 کنترل)

#### `FWPRO-STANDARDS-001` — P1 / core
- **هدف کنترل:** Record each framework version and the official source URL used for the assessment baseline.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Record each framework version and the official source URL used for the assessment baseline.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-002` — P1 / core
- **هدف کنترل:** Keep direct standards, guidance, legal obligations and adjacent references explicitly distinguished.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Keep direct standards, guidance, legal obligations and adjacent references explicitly distinguished.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-003` — P1 / core
- **هدف کنترل:** Use stable local checklist IDs and preserve official clause identifiers only where independently verified.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Use stable local checklist IDs and preserve official clause identifiers only where independently verified.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-004` — P1 / core
- **هدف کنترل:** Map each checklist item to one or more framework families with a documented mapping rationale.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Map each checklist item to one or more framework families with a documented mapping rationale.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-005` — P1 / core
- **هدف کنترل:** Record applicability decision, scope rationale and approver for every conditional control.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Record applicability decision, scope rationale and approver for every conditional control.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-006` — P1 / core
- **هدف کنترل:** Maintain status states for not assessed, compliant, partially compliant, non-compliant, not applicable, blocked and evidence pending.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Maintain status states for not assessed, compliant, partially compliant, non-compliant, not applicable, blocked and evidence pending.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-007` — P1 / core
- **هدف کنترل:** Require evidence and reviewer identity before a control can be marked compliant.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Require evidence and reviewer identity before a control can be marked compliant.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-008` — P1 / core
- **هدف کنترل:** Require written justification and approval before a control can be marked not applicable.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Require written justification and approval before a control can be marked not applicable.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-009` — P1 / core
- **هدف کنترل:** Reassess versioned standards when an official edition changes or is superseded.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Reassess versioned standards when an official edition changes or is superseded.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-010` — P1 / core
- **هدف کنترل:** Make clear that a curated crosswalk is not a complete clause-by-clause transcription or certification.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Make clear that a curated crosswalk is not a complete clause-by-clause transcription or certification.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-011` — P1 / core
- **هدف کنترل:** Track standard-to-control mapping gaps and distinguish unmapped controls from controls not tested.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Track standard-to-control mapping gaps and distinguish unmapped controls from controls not tested.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

#### `FWPRO-STANDARDS-012` — P1 / core
- **هدف کنترل:** Export a dated checklist with filters, owner, status, evidence and change history for audit review.
- **معیار پذیرش:** Run only with the documented prerequisites, approved scope and suitable specialist method; record method, version, limitations and reviewer disposition. Control objective: Export a dated checklist with filters, owner, status, evidence and change history for audit review.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_or_evidence`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `OWASP_ASVS; OWASP_WSTG; OWASP_TOP10; OWASP_API; NIST_CSF; ISO27001; ISO27002; ISO31000`
- **منابع رسمی:** [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [NIST_CSF](https://www.nist.gov/cyberframework) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27002](https://www.iso.org/standard/75652.html) · [ISO31000](https://www.iso.org/standard/65694.html)

### RELEASE — Release, operations, backup and product governance (14 کنترل)

#### `FWPRO-RELEASE-001` — P1 / core
- **هدف کنترل:** Run all required unit, contract, integration and local E2E tests before a release is tagged.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Run all required unit, contract, integration and local E2E tests before a release is tagged.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-002` — P1 / core
- **هدف کنترل:** Apply a reproducible test inventory, coverage threshold and release decision record.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Apply a reproducible test inventory, coverage threshold and release decision record.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-003` — P1 / core
- **هدف کنترل:** Test database migration/upgrade behavior and document rollback procedures.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test database migration/upgrade behavior and document rollback procedures.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-004` — P1 / core
- **هدف کنترل:** Verify Docker image build, runtime non-root posture, health checks and minimal published ports.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Verify Docker image build, runtime non-root posture, health checks and minimal published ports.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-005` — P1 / core
- **هدف کنترل:** Generate resolved SBOM and image scan results for distributable release artifacts.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Generate resolved SBOM and image scan results for distributable release artifacts.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-006` — P1 / core
- **هدف کنترل:** Sign release artifacts or publish verifiable provenance where infrastructure supports it.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Sign release artifacts or publish verifiable provenance where infrastructure supports it.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-007` — P1 / core
- **هدف کنترل:** Publish release notes, known limitations, support policy and security reporting contact.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Publish release notes, known limitations, support policy and security reporting contact.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-008` — P1 / core
- **هدف کنترل:** Protect default branch with reviews and required CI for production repositories.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Protect default branch with reviews and required CI for production repositories.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-009` — P1 / core
- **هدف کنترل:** Use minimum permissions and pinned third-party actions in CI/CD workflows.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use minimum permissions and pinned third-party actions in CI/CD workflows.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-010` — P1 / core
- **هدف کنترل:** Monitor dependency and base-image vulnerabilities and define update SLAs.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Monitor dependency and base-image vulnerabilities and define update SLAs.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-011` — P1 / core
- **هدف کنترل:** Test recovery of application database, checklist state and report evidence backups.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Test recovery of application database, checklist state and report evidence backups.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-012` — P1 / core
- **هدف کنترل:** Define product support/end-of-life policy and security update cadence.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define product support/end-of-life policy and security update cadence.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-013` — P1 / core
- **هدف کنترل:** Record release approver, source commit, build workflow, artifact hashes and deployment environment.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record release approver, source commit, build workflow, artifact hashes and deployment environment.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

#### `FWPRO-RELEASE-014` — P1 / core
- **هدف کنترل:** Perform rollback or hotfix drills for critical security defects.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Perform rollback or hotfix drills for critical security defects.
- **شواهد مورد انتظار:** Approved policy/process, responsible owner, sample records, review cadence and exceptions log.
- **روش راستی‌آزمایی:** `interview_or_evidence`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `NIST_SSDF; NIST_CSF; NIST_800_53; ISO27001; ISO27035; CIS_CONTROLS; SLSA; OPENSSF_SCORECARD; CISA_SECURE_BY_DESIGN; SLSA_PROVENANCE`
- **منابع رسمی:** [NIST_SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [NIST_CSF](https://www.nist.gov/cyberframework) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [ISO27001](https://www.iso.org/standard/27001) · [ISO27035](https://www.iso.org/standard/78973.html) · [CIS_CONTROLS](https://www.cisecurity.org/controls/v8-1) · [SLSA](https://slsa.dev/spec/v1.2/) · [OPENSSF_SCORECARD](https://openssf.org/scorecard/) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign) · [SLSA_PROVENANCE](https://in-toto.io/)

### ACCESSIBILITY_REG — Accessibility conformance governance (4 کنترل)

#### `FWPRO-ACCESSIBILITY_REG-001` — P2 / conditional
- **هدف کنترل:** Define required WCAG conformance level and applicable national/procurement accessibility obligations.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define required WCAG conformance level and applicable national/procurement accessibility obligations.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; ISO27001`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ACCESSIBILITY_REG-002` — P2 / conditional
- **هدف کنترل:** Document automated accessibility tool scope and the criteria that require manual assessment.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Document automated accessibility tool scope and the criteria that require manual assessment.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; ISO27001`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ACCESSIBILITY_REG-003` — P2 / conditional
- **هدف کنترل:** Perform manual keyboard, focus, screen-reader and cognitive/interaction review for critical workflows.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Perform manual keyboard, focus, screen-reader and cognitive/interaction review for critical workflows.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; ISO27001`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [ISO27001](https://www.iso.org/standard/27001)

#### `FWPRO-ACCESSIBILITY_REG-004` — P2 / conditional
- **هدف کنترل:** Record exceptions, remediation owners and dates for accessibility defects.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Record exceptions, remediation owners and dates for accessibility defects.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** adjacent, conditional, supporting
- **مراجع مرتبط:** `WCAG22; EN301549; ISO27001`
- **منابع رسمی:** [WCAG22](https://www.w3.org/TR/WCAG22/) · [EN301549](https://www.etsi.org/standards) · [ISO27001](https://www.iso.org/standard/27001)

### IDENTITY_PROTOCOLS — Identity protocol configuration and token lifecycle (6 کنترل)

#### `FWPRO-IDENTITY_PROTOCOLS-001` — P1 / conditional
- **هدف کنترل:** Publish and validate authorization-server metadata where supported.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Publish and validate authorization-server metadata where supported.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `NIST_800_63; OAUTH_RFC9700; JWT_RFC8725; OIDC; PKCE_RFC7636; OWASP_ASVS; NIST_800_53`
- **منابع رسمی:** [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [JWT_RFC8725](https://www.rfc-editor.org/rfc/rfc8725.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-IDENTITY_PROTOCOLS-002` — P1 / conditional
- **هدف کنترل:** Validate ID token issuer, audience, nonce, signature, expiry and token type in OIDC clients.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Validate ID token issuer, audience, nonce, signature, expiry and token type in OIDC clients.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `NIST_800_63; OAUTH_RFC9700; JWT_RFC8725; OIDC; PKCE_RFC7636; OWASP_ASVS; NIST_800_53`
- **منابع رسمی:** [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [JWT_RFC8725](https://www.rfc-editor.org/rfc/rfc8725.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-IDENTITY_PROTOCOLS-003` — P1 / conditional
- **هدف کنترل:** Reject OAuth redirect URIs that are not exact registered matches, except protocol-defined native loopback cases.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Reject OAuth redirect URIs that are not exact registered matches, except protocol-defined native loopback cases.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `NIST_800_63; OAUTH_RFC9700; JWT_RFC8725; OIDC; PKCE_RFC7636; OWASP_ASVS; NIST_800_53`
- **منابع رسمی:** [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [JWT_RFC8725](https://www.rfc-editor.org/rfc/rfc8725.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-IDENTITY_PROTOCOLS-004` — P1 / conditional
- **هدف کنترل:** Use modern OAuth flows and reject deprecated/insecure grants or response patterns where applicable.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Use modern OAuth flows and reject deprecated/insecure grants or response patterns where applicable.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `NIST_800_63; OAUTH_RFC9700; JWT_RFC8725; OIDC; PKCE_RFC7636; OWASP_ASVS; NIST_800_53`
- **منابع رسمی:** [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [JWT_RFC8725](https://www.rfc-editor.org/rfc/rfc8725.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-IDENTITY_PROTOCOLS-005` — P1 / conditional
- **هدف کنترل:** Scope access tokens narrowly and enforce audience/resource-server validation.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Scope access tokens narrowly and enforce audience/resource-server validation.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `NIST_800_63; OAUTH_RFC9700; JWT_RFC8725; OIDC; PKCE_RFC7636; OWASP_ASVS; NIST_800_53`
- **منابع رسمی:** [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [JWT_RFC8725](https://www.rfc-editor.org/rfc/rfc8725.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

#### `FWPRO-IDENTITY_PROTOCOLS-006` — P1 / conditional
- **هدف کنترل:** Define token revocation, rotation and incident handling for stolen credentials.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define token revocation, rotation and incident handling for stolen credentials.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** conditional, direct, supporting
- **مراجع مرتبط:** `NIST_800_63; OAUTH_RFC9700; JWT_RFC8725; OIDC; PKCE_RFC7636; OWASP_ASVS; NIST_800_53`
- **منابع رسمی:** [NIST_800_63](https://csrc.nist.gov/pubs/sp/800/63/4/final) · [OAUTH_RFC9700](https://www.rfc-editor.org/rfc/rfc9700.html) · [JWT_RFC8725](https://www.rfc-editor.org/rfc/rfc8725.html) · [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) · [PKCE_RFC7636](https://www.rfc-editor.org/rfc/rfc7636.html) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [NIST_800_53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

### HTTP_PROTOCOLS — Protocol correctness and edge cases (6 کنترل)

#### `FWPRO-HTTP_PROTOCOLS-001` — P2 / core
- **هدف کنترل:** Handle HTTP methods and status codes consistently with the intended resource semantics.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Handle HTTP methods and status codes consistently with the intended resource semantics.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `HTTP_RFC9110; OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; CWE_TOP25`
- **منابع رسمی:** [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-HTTP_PROTOCOLS-002` — P2 / core
- **هدف کنترل:** Reject malformed request framing and ambiguous content-length/transfer-encoding combinations at trusted gateways.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Reject malformed request framing and ambiguous content-length/transfer-encoding combinations at trusted gateways.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `HTTP_RFC9110; OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; CWE_TOP25`
- **منابع رسمی:** [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-HTTP_PROTOCOLS-003` — P2 / core
- **هدف کنترل:** Normalize header names case-insensitively without allowing duplicate security-sensitive fields to bypass policy.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Normalize header names case-insensitively without allowing duplicate security-sensitive fields to bypass policy.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `HTTP_RFC9110; OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; CWE_TOP25`
- **منابع رسمی:** [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-HTTP_PROTOCOLS-004` — P2 / core
- **هدف کنترل:** Avoid request smuggling-prone disagreement between reverse proxies and application servers.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Avoid request smuggling-prone disagreement between reverse proxies and application servers.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `HTTP_RFC9110; OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; CWE_TOP25`
- **منابع رسمی:** [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-HTTP_PROTOCOLS-005` — P2 / core
- **هدف کنترل:** Apply body/header size and timeout limits consistently across proxies and origin services.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Apply body/header size and timeout limits consistently across proxies and origin services.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `HTTP_RFC9110; OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; CWE_TOP25`
- **منابع رسمی:** [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

#### `FWPRO-HTTP_PROTOCOLS-006` — P2 / core
- **هدف کنترل:** Do not expose TRACE or unexpected administrative methods without a documented requirement.
- **معیار پذیرش:** A repeatable, bounded check produces current sanitized evidence for this control, or explicitly marks it blocked/not-tested. Finding absence alone is not proof of compliance. Control objective: Do not expose TRACE or unexpected administrative methods without a documented requirement.
- **شواهد مورد انتظار:** Bounded read-only request/response comparison, sanitized evidence and request/response identifiers.
- **روش راستی‌آزمایی:** `automated_readonly`
- **نوع رابطه با مراجع:** direct, supporting
- **مراجع مرتبط:** `HTTP_RFC9110; OWASP_WSTG; OWASP_ASVS; OWASP_TOP10; OWASP_API; CWE_TOP25`
- **منابع رسمی:** [HTTP_RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html) · [OWASP_WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/) · [OWASP_ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP_TOP10](https://owasp.org/projects/top-ten) · [OWASP_API](https://owasp.org/www-project-api-security/) · [CWE_TOP25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25)

### SUPPORT — Security support, customer communication and disclosure (5 کنترل)

#### `FWPRO-SUPPORT-001` — P2 / core
- **هدف کنترل:** Publish security contact metadata such as security.txt according to the chosen policy and RFC guidance.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Publish security contact metadata such as security.txt according to the chosen policy and RFC guidance.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; CISA_SECURE_BY_DESIGN`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign)

#### `FWPRO-SUPPORT-002` — P2 / core
- **هدف کنترل:** Provide a clear intake process for researchers with acknowledgment and safe-harbor terms where appropriate.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Provide a clear intake process for researchers with acknowledgment and safe-harbor terms where appropriate.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; CISA_SECURE_BY_DESIGN`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign)

#### `FWPRO-SUPPORT-003` — P2 / core
- **هدف کنترل:** Define coordinated disclosure timelines, customer notification criteria and embargo handling.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Define coordinated disclosure timelines, customer notification criteria and embargo handling.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; CISA_SECURE_BY_DESIGN`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign)

#### `FWPRO-SUPPORT-004` — P2 / core
- **هدف کنترل:** Ensure advisories identify affected versions, severity rationale, mitigation and fixed versions.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Ensure advisories identify affected versions, severity rationale, mitigation and fixed versions.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; CISA_SECURE_BY_DESIGN`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign)

#### `FWPRO-SUPPORT-005` — P2 / core
- **هدف کنترل:** Track external vulnerability reports through closure and feed lessons learned into product tests.
- **معیار پذیرش:** An accountable owner/reviewer confirms the control using current artifacts or reproducible test steps; exceptions have rationale, approver, compensating control and expiry. Control objective: Track external vulnerability reports through closure and feed lessons learned into product tests.
- **شواهد مورد انتظار:** Reviewer steps, expected/observed result, sanitized evidence, impact, reviewer and approval/ticket.
- **روش راستی‌آزمایی:** `manual_review`
- **نوع رابطه با مراجع:** supporting
- **مراجع مرتبط:** `ISO29147; ISO30111; NIST_800_61; CISA_SECURE_BY_DESIGN`
- **منابع رسمی:** [ISO29147](https://www.iso.org/standard/72311.html) · [ISO30111](https://www.iso.org/standard/69725.html) · [NIST_800_61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [CISA_SECURE_BY_DESIGN](https://www.cisa.gov/securebydesign)

## نکته‌ی نسخه و حق نشر

نسخه‌های مرجع در تاریخ بالا از صفحات رسمی بررسی شده‌اند؛ استانداردهای rolling/under-review ممکن است تغییر کنند. عناوین و URLها برای ارجاع هستند؛ متن‌های کنترل این فایل بازنویسی و خلاصه‌ی مستقل هستند و جایگزین متن کامل استانداردهای دارای حق نشر یا مستندات رسمی نیستند.
