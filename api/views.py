from .serializers import QuestionSerializer
from exam.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


@api_view(["GET"])
def api_list(request, *args, **kwargs):
    all_api_urls = {
        "List": "/api/list/",
        "Detail View": "/api/detail/<str:pk>/",
        "Create": "/api/create/",
        "Update": "/api/update/<str:pk>/",
        "Delete": "/api/delete/<str:pk>/",
    }
    return Response(all_api_urls)


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


@api_view(["GET"])
def exam_paper(request):
    allQuestions = []
    easy = Question.objects.filter(level='E').order_by('?')[:25]
    medium = Question.objects.filter(level='M').order_by('?')[:15]
    hard = Question.objects.filter(level='H').order_by('?')[:10]
    allQuestions.append(easy,medium,hard)
    serializer = QuestionSerializer(allQuestions, many=True)
    print("All Questions: \n",allQuestions)
    print("Serializer Data :\n",serializer.data)
    return Response(serializer.data)
