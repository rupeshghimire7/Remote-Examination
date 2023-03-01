from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
from .forms import *
import json
from faker import Faker


# Create your views here.
def home(request):
    # return HttpResponse("Homepage")
    return render(request, 'exams/home.html')

def CreateUser(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('studentlogin')
    return render(request,'exams/studentsignup.html',{'form':form})
    

def studentlogin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged in")
            return redirect('/')
        else:
            messages.error(request,"Invalid username or password")
    context={}
    return render(request,'exams/studentlogin.html',context)

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


def generate_mcqs(Question):
    fake = Faker()
    mcqs = []
    for i in range(Question):
        question = fake.sentence(nb_words=8, variable_nb_words=True, ext_word_list=None)
        correct_form = fake.word()
        options = [correct_form]
        while len(options) < 5:
            option = fake.word()
            if option not in options:
                options.append(option)
        mcqs.append({
            'question': question,
            'options': options,
            'correct_answer': correct_form
        })
    return mcqs

# def mcq_view(request):
#     mcqs = Question(10)  # generate 10 MCQs
#     context = {'mcqs': mcqs}
#     return render(request, 'mcqs.html', context)