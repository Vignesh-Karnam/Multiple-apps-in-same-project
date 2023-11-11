from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Rohit(request):
    return render(request,'Rohit.html')

def Bumrah(request):
    return HttpResponse('Bumrah is Yorker king')