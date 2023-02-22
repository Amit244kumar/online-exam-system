from django.shortcuts import render
from OTS.models import Question,User
from django.http import HttpResponseRedirect,HttpResponse
import random
from django.http import JsonResponse
# Create your views here.
"""
superuser:
username->admin
password->amit
"""
def newQuestion(request):
    try:
        if request.session['username'] == 'Admin':
           pass
        else:
            return HttpResponseRedirect('http://localhost:8000/OTS/Home/')
    except KeyError:
        return HttpResponseRedirect('http://localhost:8000/OTS/login/')
    req=render(request,'OTS/new_question.html')
    return req

def saveQuestion(request):
    question=Question()
    question.que=request.POST['quetion']
    question.optiona=request.POST['optiona']
    question.optionb=request.POST['optionb']
    question.optionc=request.POST['optionc']
    question.optiond=request.POST['optiond']
    question.answer=request.POST['answer']
    question.save()
    return HttpResponseRedirect('http://localhost:8000/OTS/view-questions/')

def viewQuestions(request):
    try:
      if request.session['username']=='Admin':
        pass
      else:
          return HttpResponseRedirect('http://localhost:8000/OTS/Home/')
    except KeyError:
         return HttpResponseRedirect('http://localhost:8000/OTS/login/')
    questions=Question.objects.all()
    res=render(request,'OTS/view_questions.html',{'questions':questions})
    return res

def editQuestion(request):
    try:
      if request.session['username']=='Admin':
          pass
      else:
          return HttpResponseRedirect('http://localhost:8000/OTS/Home/')
    except KeyError:
         return  HttpResponseRedirect('http://localhost:8000/OTS/login/')
    q=int(request.GET['que_no'])
    question=Question.objects.get(que_no=q)
    res=render(request,'OTS/edit_question.html',{'question':question})
    return res
def editSaveQuestion(request):
    question=Question()
    question.que_no=request.POST['que_no']
    question.que=request.POST['quetion']
    question.optiona=request.POST['optiona']
    question.optionb=request.POST['optionb']
    question.optionc=request.POST['optionc']
    question.optiond=request.POST['optiond']
    question.answer=request.POST['answer']
    question.save()
    return HttpResponseRedirect('http://localhost:8000/OTS/view-questions/')

def deleteQuestion(request):
    try:
        if request.session['username']=='Admin':
            pass
        else:
            return HttpResponseRedirect('http:localhost:8000/OTS/Home/')
    except KeyError:
         HttpResponseRedirect('http://localhost:8000/OTS/login/')
    question=Question.objects.filter(que_no=int(request.GET['que_no']))
    question.delete()
    return HttpResponseRedirect('http://localhost:8000/OTS/view-questions/')

def signup(request):
    d={}
    try:
        if request.GET['error']==str(1):
            d['errmsg']='user name already taken'
    except KeyError:
        d['errmsg']=''
    res=render(request,'OTS/sign_up.html',d)
    return res

def saveUser(request):
    u=User.objects.filter(username=request.POST['username'])
    if not u:
        user=User()
        user.username=request.POST['username']
        user.password=request.POST['password']
        user.realname=request.POST['realname']
        user.save()
        url='http://localhost:8000/OTS/login/'
    else:
        url='http://localhost:8000/OTS/sign-up/?error=1'
    return HttpResponseRedirect(url)

def CreateAdmin():
    user=User()
    user.username='Admin'
    user.password='password'
    user.realname='superuser'
    user.save()

def login(request):
    u=User.objects.filter(username='Admin')
    if not u:
        CreateAdmin()
    res=render(request,'OTS/login.html')
    return res

def loginValidation(request):
    try:
        u=User.objects.get(username=request.POST['username'],password=request.POST['password'])
        u.username
        request.session['username']=u.username
        request.session['realname']=u.realname
        url="http://localhost:8000/OTS/Home/"
    except:
        url='http://localhost:8000/OTS/login/'
    return HttpResponseRedirect(url)

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('http://localhost:8000/OTS/login/')

def Home(request):
    try:
        request.session['username']
    except KeyError:
        HttpResponseRedirect('http://localhost:8000/login/')
    res=render(request,'OTS/Home.html')
    return res

def startTest(request):
    try:
        request.session['username']
    except KeyError:
        return HttpResponseRedirect('http://localhost:8000/OTS/login/')
    no_of_question=5
    question_pool=list(Question.objects.all())
    random.shuffle(question_pool)
    question_list=question_pool[:no_of_question]
    res=render(request,'OTS/start_test.html',{'questions':question_list})
    return res

def testResult(request):
    try:
       request.session['username']
    except KeyError:
        return HttpResponseRedirect('http://localhost:8000/OTS/login/')
    total_question=5
    total_right=0
    total_wrong=0
    total_attempt=0
    que_no_list=[]
    for k in request.POST:
        if k.startswith("que"):
             que_no_list.append(int(request.POST[k]))
    for n in que_no_list:
         question=Question.objects.get(que_no=n)
         try:
             if question.answer == request.POST['q'+str(n)]:
                 total_right+=1
             else:
                 total_wrong+=1
             total_attempt+=1
         except:
             pass
    result={'total':total_question,
            'right':total_right,
            'wrong':total_wrong,
            'attempt':total_attempt
           }
    res=render(request,'OTS/test_result.html',result)
    return res

def forgotPassword(request):
    d={}
    try:
        request.GET['error']
        d={'error':'username not exit'}
    except KeyError:
        pass
    res=render(request,'OTS/forgot_password.html',d)
    return res

def newPasswordSave(request):
    u=User.objects.filter(username=request.POST['username'])
    if not u:
        url='http://localhost:8000/OTS/forgot-password/?error=1'
        return HttpResponseRedirect(url)
    if request.POST['password'] != request.POST['confirm-password']:
       res=render(request,'OTS/forgot_password.html',{'error':'password not matched'})
       return res
    user=User()
    user.username=request.POST['username']
    user.password=request.POST['password']
    u=User.objects.get(username=request.POST['username'])
    user.realname=u.realname
    user.save()
    url='http://localhost:8000/OTS/login/'
    return HttpResponseRedirect(url)

       