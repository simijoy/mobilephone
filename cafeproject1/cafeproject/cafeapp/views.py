from django.shortcuts import render
from . models import food

# Create your views here.
def demo(request):
    ob=food.objects.all()

    return render(request,"index.html",{'result':ob})