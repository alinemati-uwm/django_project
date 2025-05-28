from django.contrib import admin

from app.models import JobPost

class JobAdmin(admin.ModelAdmin):
    list_display= ('__str__','title','salary','date'  , 'location' ,'expiry','slug')
    list_filter= ('date','salary','expiry')
    search_fields = ('title','description')
    search_help_text = "Write in your query and hit enter"
    # fields = (('title','description'),'expiry')
    # exclude = ('title',)
    fieldsets = (
        ('Basic information', {
        'fields':('title','description')
        }),
        ('More information', {
        'classes':('collapse','wide'),
        'fields':(('expiry','salary'),'slug')
        }),
    )

# Register your models here.
admin.site.register(JobPost, JobAdmin)