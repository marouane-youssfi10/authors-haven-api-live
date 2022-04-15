from django.apps import AppConfig
from django.utils.translation import gettext as _

class FavoritesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.favorites'
    verbose_name = _("Favorites")