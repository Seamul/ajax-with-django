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
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    print(name,email,password)
    user=User(name=name,email=email,password=password)
    user.save()
    return JsonResponse({'status':"save"})
    