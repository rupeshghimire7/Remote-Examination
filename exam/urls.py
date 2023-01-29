from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('prepQ', views.makeQuestion, name='prepare'),
    path('listQ',views.listQuestion, name='list')

]
