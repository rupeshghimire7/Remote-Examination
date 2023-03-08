from .models import *
from django.contrib import admin

# Register your models here.

admin.site.register(NoticeBoard)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(User)

admin.site.register(College)
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(Level_Question)