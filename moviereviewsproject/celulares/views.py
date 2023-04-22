from django.shortcuts import render,redirect
from .models import Celulares

def celulares(request):
    celularess = Celulares.objects.all().order_by('-precio')
    return render(request, 'celulares.html', {'celularess':celularess})
