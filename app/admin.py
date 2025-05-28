from django.contrib import admin

from app.models import JobPost


# Register the JobPost model with the Django admin site
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date')


admin.site.register(JobPost, JobPostAdmin)
