from django.db import models


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
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    session = models.ForeignKey(
        AichatSession,
        related_name='requests',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    message = models.TextField()
    response = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)