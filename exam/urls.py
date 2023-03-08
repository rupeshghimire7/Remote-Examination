from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('prepQ', views.makeQuestion, name='prepare'),
    path('listQ',views.listQuestion, name='list'),
    path('studentlogin',views.studentlogin, name='studentlogin'),
    path('studentsignup',views.CreateUser,name='studentsignup'),
    path('exam',  views.generate_questions, name='exam'),
]
