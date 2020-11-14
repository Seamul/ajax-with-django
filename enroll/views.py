from django.shortcuts import render,HttpResponse
from .forms import StudentForm
# Create your views here.
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    form = StudentForm()
    stud=User.objects.all()
    return render(request,'home.html',{"form":form,"stu":stud})
# @csrf_exempt
def save_data(request):
    form= StudentForm()
    print("I am in form")
    # if form.is_valid():
    sid=request.POST.get('stuid')
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    print(name,email,password)
    
    if(sid==''):
        user=User(name=name,email=email,password=password)
        
    else:
        user=User(id=sid,name=name,email=email,password=password)
    
    user.save()

    
    student_data= User.objects.values()
    student_data=list(student_data)
    return JsonResponse({'status':"save","student_data":student_data})
    
def delete_data(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        print(id)
        pi= User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({"status":1})
    return JsonResponse({"status":0})

def edit_data(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        print(id)
        student= User.objects.get(pk=id)
        student_data={'id':student.id,'name':student.name,'email':student.email, 'password':student.password}
        return JsonResponse(student_data)
    return JsonResponse({"status":0})
