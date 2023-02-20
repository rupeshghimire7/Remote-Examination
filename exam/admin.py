from .models import NoticeBoard, Student,User, Question, College, Subject
from django.contrib import admin

# Register your models here.

admin.site.register(NoticeBoard)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(User)
admin.site.register(College)
admin.site.register(Subject)