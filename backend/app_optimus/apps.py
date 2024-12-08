from django.apps import AppConfig


class AppHomeFeedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_optimus'

class AppOptimusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_optimus'

    def ready(self):
        import sys
        if 'migrate' in sys.argv:
            from django.db.migrations.recorder import MigrationRecorder
            MigrationRecorder.migration_module = 'app_optimus.migrations_dados_db'
