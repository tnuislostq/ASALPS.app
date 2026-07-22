from django.apps import AppConfig

class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'

    def ready(self):
        # Automatically run seeding on app startup
        import sys
        if 'runserver' in sys.argv or 'gunicorn' in sys.argv:
            try:
                from .seeds import seed_database
                seed_database()
            except Exception:
                pass