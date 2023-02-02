from django.shortcuts import render
# from django.http import JsonResponse
# import json
from exam.models import *
from django.forms.models import model_to_dict

from .serializers import QuestionSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):

    instance = Question.objects.order_by("?").first()
    data = {}
    if instance:
        data = QuestionSerializer(instance).data
    # if model_question:
    #     data = model_to_dict(model_question, fields=['id','qn','correct'])

    return Response(data) 