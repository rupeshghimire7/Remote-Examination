from .models import NoticeBoard, Student,User, Question
from django.contrib import admin

# Register your models here.

admin.site.register(NoticeBoard)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(User)