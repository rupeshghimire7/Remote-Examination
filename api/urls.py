from django.urls import path
from api import views

urlpatterns = [
    # path('', views.api_home,name='api_home' ),
    path('<int:pk>/', views.QuestionAPIView.as_view()),
    path('',views.QuestionListCreateAPIView.as_view()),

]
