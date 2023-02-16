from rest_framework import serializers
from exam.models import *


# class QuestionSerializer(serializers.ModelSerializer):
#     question = serializers.SerializerMethodField(read_only = True) 
#     class Meta:
#         model = Question
#         fields = [
#             'id',
#             'correct',
#             'points',
#             # 'qn',
#             'question',
#         ]
#     def get_question(self,obj):
#         return obj.get_question()   #this get_question is a method in models of exam Question

        

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeBoard
        fields = '__all__'