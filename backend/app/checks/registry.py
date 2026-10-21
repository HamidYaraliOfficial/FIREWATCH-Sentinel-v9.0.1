from .web_checks import run_page_checks,run_form_checks,run_content_checks
from .cookie_checks import run_cookie_checks
from .cors_checks import run_cors_checks
from .advanced_checks import run_advanced_checks

def run_page_rules(page,ctx):
    out=[]
    for fn in (run_page_checks,run_form_checks,run_content_checks,run_cookie_checks,run_cors_checks,run_advanced_checks): out.extend(fn(page,ctx))
    return out
