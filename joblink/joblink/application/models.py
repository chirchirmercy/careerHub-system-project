from django.db import models

# Create your models here.
class Application(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    resume=models.CharField(max_length=100)
    requirements=models.TextField()
    applied_date=models.DateField()
    interview_date=models.DateField()
    posted_date=models.DateField()


