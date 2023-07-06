from django.db import models

# Create your models here.
class Interview(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    department=models.CharField(max_length=50)

