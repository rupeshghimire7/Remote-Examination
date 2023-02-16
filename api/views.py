from .serializers import QuestionSerializer
from exam.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):

    instance = Question.objects.order_by("?").first()
    data = {}
    if instance:
        data = QuestionSerializer(instance).data
        
    return Response(data) 


# class QuestionAPIView(generics.RetrieveAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     #it has pk as lookup field

# # question_view = QuestionAPIView.as_view()


# class QuestionListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Question.objects.all()
#     print(queryset)
#     serializer_class = QuestionSerializer

#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         serializer.save()
#         print(serializer)