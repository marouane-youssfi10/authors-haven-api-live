from django.apps import AppConfig
from django.utils.translation import gettext as _

class ReactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.reactions'
    verbose_name = _("Reactions")
