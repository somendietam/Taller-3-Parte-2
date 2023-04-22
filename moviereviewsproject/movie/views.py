from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from .models import Movie
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html', {'name':'Greg Lim'})
    #return render(request, 'home.html', {'name':'Sofia Mendieta'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies' : movies})

def about(request):
    return render(request, 'about.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password = form.cleaned_data["password1"])
            login(request, user)
            return redirect(to = "home")
        data["form"] = form

    return render(request, 'registration/registro.html', data)
