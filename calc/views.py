from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Vaibhav'})
def add(request):
    val1 = int(request.POST.get('num1'))
    val2 = int(request.POST.get('num2'))
    oprator = str(request.POST.get('op'))
    if oprator=="+":
        res = val1+val2
    if oprator=="-":
        res = val1-val2
    if oprator=="*":
        res = val1*val2
    if oprator=="/":
        res = val1/val2
    return render(request, 'result.html',{'result':res})