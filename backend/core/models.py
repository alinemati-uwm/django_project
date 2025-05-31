from openai import OpenAI
from django.db import models
from core.tasks import handle_ai_request_job
import os
import os
from openai import OpenAI
class Recipe(models.Model):
    """Represents a recipe in the system."""
    name = models.CharField(max_length=255)
    steps = models.TextField()

    def __str__(self):
        return self.name


# Model Chat Session
class ChatSession(models.Model):
    """Represents a chat session in the system."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# AI request model
class AichatSession(models.Model):
    """Represents an AI chat session in the system."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Status choices for AI requests


class AiRequest(models.Model):
    """Represents a request made to the AI in the system."""
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'
    FAILED = 'failed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (RUNNING, 'Running'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]
    status = models.CharField(
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    session = models.ForeignKey(
        AichatSession,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    message = models.JSONField()
    response = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _queue_job(self):
        """Queue the AI request job."""
        handle_ai_request_job.delay(self.id)
    # Handle for openai requests

    def handle(self):

        """Handle the AI request."""

        self.status = self.RUNNING
        self.save()
        # Simulate AI processing (replace with actual AI logic)
        print(100 * "=")
        print("Starting AI request handling...")
        print("OPENAI_API_KEY:", os.environ.get("OPENAI_API_KEY"))
        
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        print(100 * "=")
        print(self.message)
        print("Starting AI request...")
        print(100 * "=")
        print("Step 1: Preparing to send request to OpenAI...")
        try:
            print("Step 2: Sending request to OpenAI...")
            response = client.chat.completions.create(
            model="gpt-4o-mini",            
            messages=self.message
            )
            print("Step 3: Received response from OpenAI.")
            self.response = response.to_dict()
            print("Step 4: Converted response to dict.")
            self.status = self.COMPLETED
            print(100 * "=")
            print("AI request completed successfully.", response)
            print(100 * "=")
        except Exception as e:
            print("Step 5: Exception occurred during OpenAI request.")
            self.status = self.FAILED
            self.response = str(e)
            print("Error:", e)
        print("Step 6: Saving the AiRequest instance.")
        self.save()


    def save(self, **kwargs):
        """Override save method to queue the job."""
        is_new = self._state.adding
        super().save(**kwargs)
        # If this is a new instance, queue the job
        if is_new:
            self._queue_job()