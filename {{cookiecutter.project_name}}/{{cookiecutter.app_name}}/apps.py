from django.apps import AppConfig as BaseConfig
from django.utils.translation import ugettext_lazy as _


class {{cookiecutter.app_config_name}}(BaseConfig):
    name = '{{cookiecutter.app_name}}'
    verbose_name = _('{{cookiecutter.app_name.title()|replace("_", " "}}')
