from django.contrib import admin

# Register your models here.
from .models import Interview
class InterviewAdmin(admin.ModelAdmin):
    list_display=("name","email","phone_number","department")
admin.site.register(Interview,InterviewAdmin)    


