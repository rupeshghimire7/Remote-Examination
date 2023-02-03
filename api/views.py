from django.forms.models import model_to_dict

from .serializers import QuestionSerializer
from exam.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.


@api_view(["POST"])
def api_home(request, *args, **kwargs):

    instance = Question.objects.order_by("?").first()
    data = {}
    if instance:
        data = QuestionSerializer(instance).data
    # if model_question:
    #     data = model_to_dict(model_question, fields=['id','qn','correct'])

    return Response(data) 


class QuestionAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    #it has pk as lookup field

# question_view = QuestionAPIView.as_view()


