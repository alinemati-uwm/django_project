from celery import shared_task
from core import models

@shared_task
def handle_ai_request_job(ai_request_id):
    """Handle the AI request job."""
    models.AiRequest.objects.get(id=ai_request_id).handle()  # Call the handle method of the AiRequest model


@shared_task
def hello_task(name):
    print(f"Hello {name}. You have {len(name)} characters in your name.")

