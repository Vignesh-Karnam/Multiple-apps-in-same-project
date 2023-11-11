from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Virat(request):
    return render(request,'Virat.html')

def ABD(request):
    return HttpResponse('ABD is Mr.360')