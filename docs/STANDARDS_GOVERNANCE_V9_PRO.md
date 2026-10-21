# FIREWATCH Sentinel v9 — راهنمای حاکمیت چک‌لیست استانداردها

**نسخه کاتالوگ:** 9 Pro · **تاریخ بررسی منابع:** 2026-10-15  
**پوشش کاتالوگ:** 67 مرجع، 32 حوزه، 469 کنترل بازنویسی‌شده و قابل پیگیری

## 1. هدف و دامنه

این ماژول یک crosswalk قابل ممیزی برای ارزیابی امنیت اپلیکیشن وب/API و چرخه عمر امن محصول فراهم می‌کند. دامنه به استانداردهای فنی محدود نیست: برنامه‌ریزی آزمون نفوذ، SDLC، مدیریت ریسک، مدیریت آسیب‌پذیری و افشا، زنجیره تأمین نرم‌افزار، هویت و نشست، رمزنگاری/پروتکل، گزارش‌دهی، حریم خصوصی، دسترس‌پذیری، Cloud/Container، AI/LLM و الزامات صنعت/قانونیِ مشروط را نیز پوشش می‌دهد.

این مجموعه **فهرست همه استانداردهای موجود در جهان نیست**؛ اصطلاح «جامع» در این نسخه یعنی یک رجیستری گسترده و مستند از منابع منتخب مرتبط و کنترل‌های عملیاتی مرتبط با محصول. برای هر تعهد قراردادی، قانونی یا گواهی باید applicability، نسخه و بند دقیق با متن رسمی و مالک/مشاور مربوط تأیید شود.

## 2. سطوح ارتباط و applicability

- **Core / مستقیم:** مستقیماً برای تست وب/API، رفتار HTTP، امنیت برنامه، پروتکل‌ها یا خروجی‌های FIREWATCH مرتبط است.
- **Conditional / مشروط:** فقط هنگامی اعمال می‌شود که فناوری، نوع داده، صنعت، کشور، مشتری یا مدل استقرار مربوط باشد؛ از جمله PCI DSS، GDPR، NIS2، DORA، HIPAA، SOC 2، موبایل، AI/LLM و کنترل‌های Cloud.
- **Adjacent / مجاور:** ممکن است از نظر کیفیت محصول، دسترس‌پذیری، طراحی امن یا عملیات ارزشمند باشد، ولی معادل کنترل آسیب‌پذیری وب نیست.
- **Supporting / پشتیبان:** برای مدیریت امنیت، توسعه امن، پاسخ‌گویی به رخداد، ریسک و زنجیره تأمین کمک می‌کند.

طبقه‌بندی رجیستری برای اولویت‌بندی است، نه تفسیر حقوقی نهایی. بعضی منابع دارای وضعیت زنده/چرخان هستند؛ edition و errata باید قبل از هر engagement دوباره بررسی شوند.

## 3. وضعیت‌ها و معنی آن‌ها

| مقدار API | معنی | شرط استفاده |
|---|---|---|
| `not_assessed` | هنوز بررسی نشده | مقدار پیش‌فرض؛ هیچ استنباط پاس/فیل ندارد |
| `evidence_pending` | نتیجه یا مدرک در انتظار | تا تکمیل شواهد، پاس محسوب نمی‌شود |
| `blocked` | ارزیابی متوقف/مسدود است | علت، مالک رفع مانع و در صورت نیاز تاریخ هدف ثبت شود |
| `compliant` | کنترل در دامنه‌ی تعریف‌شده منطبق ارزیابی شده | شواهد + مالک + بازبین لازم است؛ برای انطباق حقوقی/گواهی مستقل کافی نیست |
| `partially_compliant` | بخشی از معیار رعایت شده | دامنه‌ی رعایت و شکاف‌ها باید مستند شوند؛ شواهد + مالک + بازبین لازم است |
| `non_compliant` | شواهد نشان‌دهنده‌ی شکاف است | اثر، ریسک، برنامه اصلاح و موعد لازم است؛ شواهد + مالک + بازبین لازم است |
| `not_applicable` | به دامنه/سامانه اعمال نمی‌شود | توجیه مستند حداقل 20 نویسه و بازبین لازم است؛ N/A برای دور زدن کنترل ممنوع است |

**قانون طلایی:** «اسکنر یافته‌ای گزارش نکرد» به معنی `compliant` نیست. کنترل‌های دستی، مصاحبه‌ای یا نیازمند حساب/محیط آزمایش باید با evidence صریح و بازبین مستقل بسته شوند.

## 4. گردش کار صنعتی پیشنهادی

1. **تعریف engagement:** شناسه پروژه، مالک سامانه، دامنه، میزبان‌ها/پورت‌ها، محیط، زمان، روش‌های مجاز، مسیرهای مستثنا، سقف درخواست و تماس اضطراری را ثبت کنید.
2. **Applicability review:** رجیستری 67 مرجع را بررسی کنید؛ قوانین و schemeهای مشروط را با مسئول حقوقی/حریم خصوصی/صنعت تأیید کنید.
3. **Baseline assessment:** روی محیط مجاز، نسخه/commit، پیکربندی و تاریخ اسکن را ثبت کنید؛ در صورت امکان baseline قبل از تغییرات نگه دارید.
4. **Evidence collection:** هر شاهد باید به کنترل خاص، asset/version، تاریخ، مرحله و نتیجه‌ی قابل بازتولید متصل باشد. داده‌های شخصی و secretها را حذف/ماسک کنید.
5. **Independent review:** بازبین باید مستقل از اجراکننده باشد یا استقلال/استثنا توجیه شود. فیلد reviewer در API متن آزاد است و به تنهایی اثبات هویت نیست.
6. **Disposition:** `compliant`، `partial`، `non_compliant` یا `N/A` را با شواهد ثبت کنید؛ برای استثناها مالک ریسک، جبران‌کننده و تاریخ انقضا نگه دارید.
7. **Remediation / retest:** شکاف را به ticket متصل کنید، اصلاح را در build جدید دوباره تست کنید و وضعیت قبلی را در تاریخچه حفظ کنید.
8. **Release gate:** قبل از انتشار گزارش، کاتالوگ و نسخه منابع را بازبینی کنید؛ ZIP، workbook و CSV را از نظر نشت داده و یکپارچگی بررسی کنید.
9. **Periodic refresh:** حداقل فصلی، و نیز هنگام انتشار edition جدید یا تغییر قانون/مشتری/معماری، رجیستری را بازبینی کنید.

## 5. شواهد قابل قبول و کیفیت شواهد

شاهد می‌تواند شامل نتیجه تست قابل بازتولید، گزارش اسکن و نسخه ابزار، capture پاک‌سازی‌شده HTTP، پیکربندی، policy، approval ticket، CI run، SBOM/attestation، لاگ ممیزی، نتیجه بازبینی کد یا مصاحبه ثبت‌شده باشد. برای هر شاهد این موارد را در نظر بگیرید:

- مرتبط بودن مستقیم با معیار پذیرش، asset و نسخه/commit مشخص؛
- timestamp، اجراکننده، reviewer، محیط و ابزار/نسخه؛
- محرمانگی و حداقل‌سازی داده، redaction و کنترل دسترسی؛
- hash یا امضای مستقل برای artifactهای مهم؛
- قابلیت بازتولید و تاریخ انقضا/تازگی؛
- تفکیک مشاهده‌ی ابزار از تفسیر انسان و از نتیجه‌ی حقوقی/گواهی.

URL شاهد نباید شامل user-info یا query پارامترهای حساس/توکن باشد. از پیوند به مخزن داخلی با کنترل دسترسی استفاده کنید؛ محتویات حساس را مستقیماً در note ذخیره نکنید.

## 6. پوشش استاندارد و محدودیت خودکارسازی

کنترل‌ها دارای `verification_mode` هستند؛ از جمله `automated_passive`، `automated_readonly`، `automated_plus_manual`، `manual_review`، `interview_or_evidence`، `external_tool` و `specialist_tool`. وجود در چک‌لیست به معنی اجرای خودکار نیست. هر مورد باید به test implementation، manual procedure، یا external tool صریح متصل شود.

در این بسته، crosswalk و tracker موجودند؛ این موضوع به‌تنهایی به معنی پیاده‌سازی همه کنترل‌های OWASP ASVS/WSTG/NIST/ISO یا تست کامل BOLA/IDOR، منطق کسب‌وکار، سوءاستفاده‌ی حساب، موبایل، Cloud، نفوذ عمیق یا انطباق قانونی نیست. مواردی که نیازمند احراز هویت چندنقشی، داده آزمایشی، ابزار تخصصی یا بازبینی انسانی هستند باید همین‌طور گزارش شوند.

## 7. گروه‌های منبع در رجیستری

- **App/Web/API:** OWASP ASVS، WSTG، OWASP Top 10، API Security Top 10، Cheat Sheet Series، SAMM، OpenAPI و JSON Schema.
- **هویت/وب/پروتکل:** NIST SP 800-63، OAuth 2.0 Security BCP، OIDC، PKCE، JWT BCP، HTTP Semantics، TLS 1.3/TLS BCP، HSTS، Cookies، CSP و SRI.
- **حاکمیت/ریسک/SDLC:** NIST CSF، SSDF، SP 800-53، SP 800-115، ISO/IEC 27001/27002/27034، ISO 31000، CIS Controls، CISA Secure by Design و OWASP SAMM.
- **Privacy/sector:** GDPR، NIS2، DORA، PCI DSS، HIPAA، SOC 2، ISO/IEC 27701. applicability نیازمند تحلیل حقوقی و سازمانی است.
- **Supply chain/response:** CycloneDX، SPDX، SLSA، in-toto، OpenSSF Scorecard، ISO/IEC 29147/30111/27035، CVSS، EPSS، CISA KEV، CWE Top 25، CAPEC و MITRE ATT&CK.
- **Conditional technology:** MASVS/MASTG برای موبایل، Cloud-Native/ CIS Benchmarks/ISO 27017 برای زیرساخت، OWASP LLM Top 10/NIST AI RMF/ISO 42001 برای قابلیت‌های AI.
- **Quality/accessibility:** WCAG 2.2 و EN 301 549؛ مجاور/مشروط، نه جایگزین تست امنیت.

فهرست کامل editionها، روابط و لینک‌های رسمی در `standards/standards_registry.json` و workbook قابل فیلتر ثبت شده است.

## 8. API و یکپارچه‌سازی

- `GET /api/v1/standards/registry` — فهرست منابع/نسخه‌ها و لینک‌ها.
- `GET /api/v1/standards/summary?project_key=default` — خلاصه پیشرفت کنترل‌ها برای پروژه.
- `GET /api/v1/standards/checklist` — فهرست صفحه‌بندی‌شده؛ فیلتر بر اساس framework، domain، priority، applicability، status، verification mode، relationship (`direct`/`supporting`/`conditional`/`adjacent`) و search.
- `PATCH /api/v1/standards/checklist/{control_id}` — ثبت وضعیت و شواهد با optimistic concurrency (`expected_revision`).
- `GET /api/v1/standards/checklist/{control_id}/history` — تاریخچه وضعیت‌ها.
- `GET /api/v1/standards/checklist/export.csv` — CSV با UTF-8 BOM و محافظت در برابر formula injection.
- `GET /api/v1/standards/workbook` — دانلود workbook Excel تحت API key.
- `/standards/STANDARDS_CHECKLIST.md` — نسخه متنی قابل مرور.

اگر `FIREWATCH_API_KEY` تنظیم شده باشد، درخواست API باید هدر `X-API-Key` ارسال کند. production باید با API key قوی، TLS، هویت واقعی در لایه‌ی reverse proxy/SSO، دیتابیس، backup، retention و RBAC عملیاتی شود. فیلدهای owner/reviewer/updated_by ورودی متنی‌اند؛ بدون یکپارچه‌سازی هویت، به‌تنهایی اثبات‌کننده‌ی هویت نیستند.

## 9. فایل‌ها و نقش هر کدام

- `standards/standards_registry.json`: مرجع frameworkها، edition، applicability و URL رسمی.
- `standards/standards_checklist.json`: تعریف کانونی 469 control.
- `standards/standards_checklist.csv`: خروجی عمومیِ ثابت برای تحلیل آفلاین.
- `standards/standards_checklist_summary.json`: خلاصه شمارش کاتالوگ.
- `standards/STANDARDS_CHECKLIST.md`: راهنمای انسانی و جدول منبع‌ها.
- `standards/FIREWATCH_Standards_Checklist_v9_Pro.xlsx`: tracker آفلاین با Dashboard، Master Checklist، Registry، Domain Summary و Methodology.
- `tools/generate_standards_catalog.py`: بازتولید فایل‌های کاتالوگ از source definitions.
- `backend/app/standards_catalog.py`: بارگذاری و اعتبارسنجی کاتالوگ و merge وضعیت پروژه.
- `backend/app/standards_schemas.py`: schema و validation ورودی وضعیت.
- `backend/app/models.py`: وضعیت و تاریخچه‌ی پروژه در DB.
- `backend/tests/test_standards_checklist_api.py`: تست endpointها و قرارداد ذخیره وضعیت.

**توجه درباره workbook:** workbook یک snapshot آفلاین برای جلسه‌های audit/Excel است و خودکار با DB همگام نمی‌شود. برای وضعیت زنده از داشبورد/API استفاده کنید؛ برای workbook تازه آن را مجدداً از نسخه‌ی جاری دریافت کنید.

## 10. منبع رسمی را چطور تأیید کنیم؟

همیشه edition را از ناشر رسمی بررسی کنید. نمونه‌ی baselineهای اصلی این کاتالوگ: OWASP ASVS 5.0.0 stable و WSTG v4.2 stable؛ OWASP Top 10 2025 و OWASP API Security Top 10 2023 منابع آگاهی/راهنما هستند، نه گواهی انطباق. برای رجیستری کامل، URL رسمی کنار هر ورودی است. استانداردهای ISO و بعضی schemeهای صنعتی ممکن است متن normatively licensed/paid داشته باشند؛ برای claim رسمی متن مجاز/خریداری‌شده و ارزیاب صلاحیت‌دار لازم است.

## 11. Tenancy and authorization boundary

`project_key` partitions checklist state in the data model but **is not an authorization boundary**. The current API-key gate is a shared service-level gate; it does not implement organization membership, per-project roles, SSO/SCIM, or tenant-level authorization. Do not expose this instance to multiple mutually untrusted customers until an authenticated identity layer and per-project RBAC/ABAC checks are implemented and tested. On a single-team deployment, place the service behind an access-controlled network/reverse proxy and configure a strong API key over TLS.
