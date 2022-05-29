from collections.abc import Iterable
from typing import Any

class FormatChecker:
    checkers: Any
    def __init__(self, formats: Iterable[str] | None = ...) -> None: ...
    def checks(self, format, raises=...): ...
    cls_checks: Any
    def check(self, instance, format) -> None: ...
    def conforms(self, instance, format) -> bool: ...

draft3_format_checker: FormatChecker
draft4_format_checker: FormatChecker
draft6_format_checker: FormatChecker
draft7_format_checker: FormatChecker
draft201909_format_checker: FormatChecker
draft202012_format_checker: FormatChecker

def is_email(instance) -> bool: ...
def is_ipv4(instance) -> bool: ...
def is_ipv6(instance) -> bool: ...

# is_host_name is only defined if fqdn is installed.
def is_host_name(instance) -> bool: ...
def is_idn_host_name(instance) -> bool: ...
def is_uri(instance) -> bool: ...
def is_uri_reference(instance) -> bool: ...
def is_iri(instance) -> bool: ...
def is_iri_reference(instance) -> bool: ...
def is_datetime(instance) -> bool: ...
def is_time(instance) -> bool: ...
def is_regex(instance) -> bool: ...
def is_date(instance) -> bool: ...
def is_draft3_time(instance) -> bool: ...
def is_css_color_code(instance) -> bool: ...
def is_css21_color(instance) -> bool: ...
def is_json_pointer(instance) -> bool: ...
def is_relative_json_pointer(instance) -> bool: ...
def is_uri_template(instance) -> bool: ...

# is_duration is only defined if isoduration is installed.
def is_duration(instance) -> bool: ...
def is_uuid(instance) -> bool: ...
