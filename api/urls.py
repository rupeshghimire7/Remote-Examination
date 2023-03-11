from django.urls import path
from api import views

urlpatterns = [
    path('', views.api_home,name='api_home' ),
    path('list/', views.api_list,name='api_list' ),
    path('exampaper/', views.exam_paper,name='exam_paper' ),
#     path('<int:pk>/', views.QuestionAPIView.as_view()),
#     path('',views.QuestionListCreateAPIView.as_view()),
]
