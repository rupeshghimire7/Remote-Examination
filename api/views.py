from django.shortcuts import render
# from django.http import JsonResponse
# import json
from exam.models import *
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    model_question = Question.objects.order_by("?").first()
    data = {}
    if model_question:
        data = model_to_dict(model_question, fields=['id','qn','correct'])
#        json_data_str = json.dumps(data)  #serialiable
#        return HttpResponse(json_data_str,headers={"content-type":"appl
# "})
        # data['id'] = model_question.id]
        # data['question'] = model_question.qn
        # data["correct"] = model_question.correct
        # data["points"] = model_question.points
    return Response(data) 