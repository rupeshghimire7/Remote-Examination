from django import forms
from django.core import validators
from .models import Question, Student



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'



# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['avatar', 'name', 'username', 'email', 'bio']