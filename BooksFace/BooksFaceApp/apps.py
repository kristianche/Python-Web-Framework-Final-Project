from django.apps import AppConfig


class BooksFaceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BooksFace.BooksFaceApp'

    def ready(self):
        from BooksFace.BooksFaceApp.signals import after_created_user, after_updated_profile, after_delete_profile
