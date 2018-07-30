from django.shortcuts import render

def home(request):
    return render(request,'wiki/home.html')

# Create your views here.
