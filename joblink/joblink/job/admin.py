from django.contrib import admin

# Register your models here.
from .models import Job
class JobAdmin(admin.ModelAdmin):
    list_display=("tittle","description","location","created_at")
admin.site.register(Job,JobAdmin) 