from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator



class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=100,null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(unique=True,null=True)
    avatar = models.ImageField(null=True, default='avatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




class NoticeBoard(models.Model):
    notice = models.CharField(max_length = 1500,blank=True, default=" ")

    def __str__(self) -> str:
        return self.notice[:60]



class Question(models.Model):
    qn = models.CharField(max_length=500,default="x")
    correct = models.CharField(max_length=200,default="x")
    points = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(2), MinValueValidator(1)])

    def __str__(self) -> str:
        return self.qn[:50]


class Answer(models.Model):
    options = models.TextField(default='y')
    question = models.ForeignKey(Question ,on_delete=models.CASCADE, default="", null=False)



class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(default=16)
    roll = models.CharField(default='PAS076BCT025',max_length=12)



    def __str__(self):
        return self.name
