from django.contrib import admin

# Register your models here.


from .models import Application
class ApplicationAdmin(admin.ModelAdmin):
    list_display=("name","email","phone_number","resume","requirements","applied_date","posted_date","interview_date",)
admin.site.register(Application,ApplicationAdmin) 