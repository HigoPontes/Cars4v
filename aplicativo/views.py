from django.shortcuts import render

from aplicativo.models import Cars

# Create your views here.
def index(request):
    cars = Cars.objects.all()
    return render(request, 'index.html',{'cars': cars})