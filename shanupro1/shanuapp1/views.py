from django.shortcuts import render
from django.http import HttpResponse

from shanuapp1.models import Student
from .models import User
from .forms import StudentRegistration
from .models import Student1
from django.contrib import messages

from .models import Student2,Teacher,Contractor

# Create your views here.
def learn(request):
    return HttpResponse('<h1>Hello Django</h1>')

def code(request):
    return HttpResponse('Back to work..')

def template(request):
    return render(request,'index.html')

def dynamic_temp(request):
    data={
        'titles':'django web pages',
        'content':'Welcome to shanu web page',
        'end':'Thank you..'
    }
    return render(request,'result.html',data)

def if_stat(request):
    data1={
        'titlee':'Django',
        'numbers':[10,20,30,40,50]
    }
    return render(request,'if-else.html',data1)

def loop(request):
    data2={
        'names':['shanu','bhai','hello','world']
    }
    return render(request,'loop.html',data2)

def statics(request):
    data3={
        'titled':'Django',
        'cname':'Frameworkssss'
    }
    return render(request,'stat.html',data3)

def temp_home(request):
    return render(request,'home.html')

def temp_about(request):
    return render(request,'about.html')

def temp_courseinfo(request):
    return render(request,'courseinfo.html')

def studentinfo(request):
    stu=Student.objects.all()
    return render(request,'studetails.html',{'stu':stu})

def showformdata(request):

    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
    else:
        fm=StudentRegistration()
    return render(request,'user_reg.html',{'form':fm})

def dynamic_url1(request):
    return HttpResponse('hello this is dynamic url basic')

def dynamic_url2(request,idd):
    return HttpResponse(idd)


def regi(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            
            messages.success(request,"your account is created..")
            messages.info(request,"your can login your account...")
            messages.warning(request,"your account is not create...")
            messages.debug(request,"this is debug..")

    else:
        fm=StudentRegistration()
    return render(request,'user-reg1.html',{'form':fm})

# Yaha se cookies start hai 

def setcookie(request):
    response=render(request,'setcookie.html')
    response.set_cookie('name','Shanu')
    return response

def getcookie(request):
    name=request.COOKIES['name']
    return render(request,'getcookie.html',{'name':name})

def delcookie(request):
    respone=render(request,'delcookie.html')
    respone.delete_cookie('name')
    return respone

# session framework hai yeah cookie ke terah similar hai..

def setsession(request):
    request.session['name']='Nasrullah'
    return render(request,'setsession.html')

def getsession(request):
    name=request.session['name']
    return render(request,'getsession.html',{'name':name})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'delsession.html')

# MiddleWare hai yeah

def m_home(request):
    print("I am view")
    return HttpResponse("This is M.W page..")

def q_home(request):
    student_data=Student1.objects.all()

    #student_data=Student1.objects.filter(marks=70)

    #student_data=Student1.objects.exclude(marks=70)

    #student_data=Student1.objects.order_by('city')

    #student_data=Student1.objects.order_by('-marks')

    #student_data=Student1.objects.order_by('id').reverse()

    #student_data=Student1.objects.dates('pass_date','month')



    print("SQL QUERY:-",student_data.query)

    return render(request,'qhome.html',{'students':student_data})



def model_home(request):
    student_data1=Student2.objects.all()
    teacher_data=Teacher.objects.all()
    contractor_data=Contractor.objects.all()
    return render(request,'modelhome.html',{'students':student_data1,
    'teachers':teacher_data,'contractors':contractor_data})