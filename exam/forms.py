from django import forms
from django.core import validators
from .models import Question, Student, Answer



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['correct']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["question"]


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['avatar', 'name', 'username', 'email', 'bio']