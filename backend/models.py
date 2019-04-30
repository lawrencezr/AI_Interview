from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    actual_name = models.CharField(max_length=255)


class Admin(models.Model):
    admin_name = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)


class Interview_Authority(models.Model):
    name = models.CharField(max_length=255)
    interview_code=models.CharField(max_length=255)

