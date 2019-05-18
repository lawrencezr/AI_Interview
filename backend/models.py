from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    actual_name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)


class Admin(models.Model):
    admin_name = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)


class Interview(models.Model):
    interview_code = models.CharField(max_length=5,primary_key=True)
    company = models.CharField(max_length=20)
    job = models.CharField(max_length=20)


class Interview_Authority(models.Model):
    name = models.CharField(max_length=20)
    interview = models.ManyToManyField(Interview, related_name='面试授权')


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    interview = models.ManyToManyField(Interview, related_name='问题')


class Video(models.Model):
    interview_code = models.CharField(max_length=5)
    url = models.CharField(max_length=255)
    beauty = models.IntegerField(null=True, blank=True)
    emotion = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='求职者信息')


class Performance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='求职者成绩')
    interview_code = models.CharField(max_length=5)
    grade = models.IntegerField()



class Test_Video(models.Model):
    admin = models.ManyToManyField(Admin,related_name='面试官信息')
    interview_code = models.CharField(max_length=5)
    url = models.CharField(max_length=255)
    beauty = models.IntegerField()
    emotion = models.IntegerField()
    affinity = models.IntegerField()
