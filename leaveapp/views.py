from django.shortcuts import render


def index(request):
    return render(request,'abc.html')

def hello(request):
    return render(request,'def.html')

