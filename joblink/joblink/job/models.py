from django.db import models

# Create your models here.
class Job(models.Model):
    tittle=models.CharField(max_length=100)
    description=models.TextField()
   
    location=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
   



