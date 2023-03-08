from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator



class User(AbstractUser):
    username = models.CharField(max_length=100,blank=False,default="username")
    email = models.EmailField(unique=True,default="student@example.com",blank=False)
    password = models.CharField(max_length=10,blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __self__(self):
        return self.username


class Subject(models.Model):
    subject = models.CharField(max_length=50,null=True,blank=False)
    # SubCode = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name


class College(models.Model):
    college = models.CharField(max_length=200,null=True,blank=False)
    code = models.CharField(max_length=5,null=True,blank=False)

    def __str__(self):
        return f"{self.code} ----->>  {self.college} "



class NoticeBoard(models.Model):
    title = models.CharField(max_length=50,default="Title")
    notice = models.CharField(max_length = 1500,blank=True, default=" ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


LEVEL_CHOICES = (
    ('H','Hard'),
    ('M','Medium'),
    ('E','Easy'),
)
class Question(models.Model):
    level = models.CharField(max_length = 1, choices=LEVEL_CHOICES,default="M",blank=False)
    question = models.CharField(max_length=500,default="x",blank=False)
    correct = models.CharField(max_length=200,default="x", blank=False)
    options = models.TextField(default='options')
    points = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self) -> str:
        return self.qn[:50]


    def get_question(self):
        return self.qn

class Exam(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)
    
    def __str__(self):
        return self.title
    

class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(default=16)
    roll = models.CharField(default='PAS076BCT025',max_length=12)
    avatar = models.ImageField(null=True, default='avatar.svg')
    bio = models.TextField(null=True)


    def __str__(self):
        return self.name

