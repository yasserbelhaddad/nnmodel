from django.apps import AppConfig
from api.eureka_config import run_eureka_client

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    def ready(self):
        # Start the Eureka client when the app is ready
        run_eureka_client()