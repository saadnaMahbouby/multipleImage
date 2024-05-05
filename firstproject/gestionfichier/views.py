from django.shortcuts import render, redirect
from .forms import UploadImageForm
from .models import UploadImage
from django.contrib.auth import logout
from .models import Annonce
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url='login')
def upload_photo(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Créer une nouvelle annonce
            annonce = Annonce.objects.create(
                user = request.user,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description']
            )
            # Enregistrer les images associées à l'annonce
            files = request.FILES.getlist('image')
            for file in files:
                UploadImage.objects.create(
                    annonce=annonce,
                    image=file
                )
            return redirect('photo_list')
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})

@login_required(login_url='login')
def photo_list(request):
    annonces = Annonce.objects.filter(user=request.user)
    return render(request, 'show_files.html', {'annonces': annonces})
def home(request):
    annonces = Annonce.objects.all()
    return render(request, 'index.html', {'annonces': annonces})

@login_required
def user_announces(request):
    # Récupérer les annonces de l'utilisateur connecté
    annonces = Annonce.objects.filter(user=request.user)
    return render(request, 'user_announces.html', {'annonces': annonces})

def delete_all_photos(request):
    UploadImage.objects.all().delete()
    return redirect('photo_list')

def delete_photo(request, photo_id):
    photo = UploadImage.objects.get(pk=photo_id)
    photo.delete()
    return redirect('photo_list')
def delete_annonce(request, annonce_id):
    annonce = Annonce.objects.get( pk=annonce_id)
    annonce.delete()
    return redirect('photo_list')


def search(request):
    query = request.GET.get('q')
    annonces = Annonce.objects.filter(title__icontains=query)  # Filtrez les annonces par titre
    return render(request, 'index.html', {'annonces': annonces})

@login_required(login_url='login')
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

# views.py

class CustomLoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        # Récupérer les données du formulaire
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        # Authentifier l'utilisateur
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            # Si l'utilisateur existe et les informations d'identification sont correctes, connectez-vous
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            # Si l'authentification échoue, redirigez l'utilisateur vers la page de connexion
            return HttpResponseRedirect(reverse('login'))

    def get_success_url(self):
        # Rediriger l'utilisateur vers votre chemin de profil après la connexion réussie
        return reverse('home')
    
def CustomLogoutView(request):
    logout(request)
    return redirect('home')  


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirection vers l'URL souhaité après le signup
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})