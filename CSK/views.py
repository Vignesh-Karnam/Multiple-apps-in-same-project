from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Msd(request):
    return render(request,'Msd.html')

def Raina(request):
    return HttpResponse('<h1>Raina is Mr.IPL</h1>')