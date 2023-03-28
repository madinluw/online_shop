from django.shortcuts import render
from .models import NewBalance
# Create your views here.

def main(req):
    nike = NewBalance.objects.all()
    context  = {'Nike':nike}
    return render(req, 'index.html', context)

def detail(req):
    return render(req, 'detail.html')