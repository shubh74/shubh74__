import sys
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Type, Union

from django.apps.config import AppConfig
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import CheckMessage
from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.urls import URLPattern, URLResolver
from django.utils.functional import LazyObject

if sys.version_info >= (3, 9):
    from weakref import WeakSet

    all_sites: WeakSet[AdminSite]
else:
    from typing import MutableSet

    all_sites: MutableSet[AdminSite]

_ActionCallback = Callable[[ModelAdmin, HttpRequest, QuerySet], Optional[TemplateResponse]]

class AlreadyRegistered(Exception): ...
class NotRegistered(Exception): ...

class AdminSite:
    site_title: str = ...
    site_header: str = ...
    index_title: str = ...
    site_url: str = ...
    login_form: Optional[Type[AuthenticationForm]] = ...
    index_template: Optional[str] = ...
    app_index_template: Optional[str] = ...
    login_template: Optional[str] = ...
    logout_template: Optional[str] = ...
    password_change_template: Optional[str] = ...
    password_change_done_template: Optional[str] = ...
    name: str = ...
    enable_nav_sidebar: bool = ...
    empty_value_display: str = ...
    final_catch_all_view: bool = ...
    _empty_value_display: str = ...
    _registry: Dict[Type[Model], ModelAdmin]
    _global_actions: Dict[str, _ActionCallback]
    _actions: Dict[str, _ActionCallback]
    def __init__(self, name: str = ...) -> None: ...
    def check(self, app_configs: Optional[Iterable[AppConfig]]) -> List[CheckMessage]: ...
    def register(
        self,
        model_or_iterable: Union[Type[Model], Iterable[Type[Model]]],
        admin_class: Optional[Type[ModelAdmin]] = ...,
        **options: Any
    ) -> None: ...
    def unregister(self, model_or_iterable: Union[Type[Model], Iterable[Type[Model]]]) -> None: ...
    def is_registered(self, model: Type[Model]) -> bool: ...
    def add_action(self, action: _ActionCallback, name: Optional[str] = ...) -> None: ...
    def disable_action(self, name: str) -> None: ...
    def get_action(self, name: str) -> Callable: ...
    @property
    def actions(self) -> Iterable[Tuple[str, _ActionCallback]]: ...
    def has_permission(self, request: HttpRequest) -> bool: ...
    def admin_view(self, view: Callable, cacheable: bool = ...) -> Callable: ...
    def get_urls(self) -> List[Union[URLResolver, URLPattern]]: ...
    @property
    def urls(self) -> Tuple[List[Union[URLResolver, URLPattern]], str, str]: ...
    def each_context(self, request: HttpRequest) -> Dict[str, Any]: ...
    def password_change(
        self, request: HttpRequest, extra_context: Optional[Dict[str, Any]] = ...
    ) -> TemplateResponse: ...
    def password_change_done(
        self, request: HttpRequest, extra_context: Optional[Dict[str, Any]] = ...
    ) -> TemplateResponse: ...
    def i18n_javascript(self, request: HttpRequest, extra_context: Optional[Dict[str, Any]] = ...) -> HttpResponse: ...
    def logout(self, request: HttpRequest, extra_context: Optional[Dict[str, Any]] = ...) -> TemplateResponse: ...
    def login(self, request: HttpRequest, extra_context: Optional[Dict[str, Any]] = ...) -> HttpResponse: ...
    def _build_app_dict(self, request: HttpRequest, label: Optional[str] = ...) -> Dict[str, Any]: ...
    def get_app_list(self, request: HttpRequest) -> List[Any]: ...
    def index(self, request: HttpRequest, extra_context: Optional[Dict[str, Any]] = ...) -> TemplateResponse: ...
    def app_index(
        self, request: HttpRequest, app_label: str, extra_context: Optional[Dict[str, Any]] = ...
    ) -> TemplateResponse: ...
    def autocomplete_view(self, request: HttpRequest) -> HttpResponse: ...
    def catch_all_view(self, request: HttpRequest, url: str) -> HttpResponse: ...

class DefaultAdminSite(LazyObject): ...

site: AdminSite