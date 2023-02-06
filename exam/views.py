from django.shortcuts import render, HttpResponse, redirect
from .models import Student, Question, Answer
from .forms import QuestionForm, AnswerForm, StudentForm
import json

# Create your views here.
def home(request):
    # return HttpResponse("Homepage")
    return render(request, 'exams/home.html')




def makeQuestion(request):
    if request.method == 'POST':
        qn_form = request.POST.get('question')
        opt1 = request.POST.get('option1')
        opt2 = request.POST.get('option2')
        opt3 = request.POST.get('option3')
        opt4 = request.POST.get('option4')
        pt = request.POST.get('points')

        correct_form = opt1
        option = [opt1, opt2, opt3, opt4]

        print(qn_form,opt1,opt2,opt3,opt4,option,correct_form)

        q = Question.objects.create(question=qn_form, correct = correct_form, points=pt, options = json.dumps(option))
        q.save()
        return redirect('list')
            

    return render(request, 'exams/prepareQ.html')





def listQuestion(request):    

    questions = Question.objects.all()
    jsonDec = json.decoder.JSONDecoder()


    return render(request,'exams/listQ.html',{'questions':questions})
