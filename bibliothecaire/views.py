from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Membre, Emprunt, Livre, CD, DVD, JeuDePlateau
from .forms import MembreForm, EmpruntForm, BibliothecaireLoginForm, CDForm, DVDForm, LivreForm, JeuForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#Connexion Bibliothécaire
def bibliothecaire_login(request):
    form = BibliothecaireLoginForm(request, data=request.POST or None)
    print("Form created.")

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('bibliothecaire:dashboard')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'login.html', {'form': form})


# Tableau de bord
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# Liste des membres
@login_required
def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'liste_membres.html', {'membres': membres})

# Ajouter un membre
@login_required
def ajouter_membre(request):
    form = MembreForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Membre créé avec succès !")
        return redirect('bibliothecaire:liste_membres')
    return render(request, 'ajouter_membre.html', {'form': form})

# Modifier un membre
@login_required
def modifier_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    form = MembreForm(request.POST or None, instance=membre)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Membre modifié avec succès !")
        return redirect('bibliothecaire:liste_membres')
    return render(request, 'modifier_membres.html', {'form': form})

# Supprimer un membre
@login_required
def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    membre.delete()
    messages.success(request, "Membre supprimé avec succès !")
    return redirect('bibliothecaire:liste_membres')

# Liste des CDs
def liste_cds(request):
    cds = CD.objects.all()
    return render(request, 'medias/cds/liste.html', {'cds': cds})

# Ajouter un CD
def ajouter_cd(request):
    form = CDForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "cd créé avec succès !")
    return render(request, 'ajouter_cd.html',{'form': form})

# Liste des DVDs
def liste_dvds(request):
    dvds = DVD.objects.all()
    return render(request, 'medias/dvds/liste.html', {'dvds': dvds})

# Ajouter un DVD
def ajouter_dvd(request):
    form = DVDForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "DVD créé avec succès !")
    return render(request, 'ajouter_dvd.html',{'form': form})

# Liste des livres
def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'medias/livres/liste.html', {'livres': livres})

# Ajouter un livre
def ajouter_livre(request):
    form = LivreForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Livre créé avec succès !")
    return render(request, 'ajouter_livre.html',{'form': form})

# Liste des Jeux
def liste_jeux(request):
    jeux = JeuDePlateau.objects.all()
    return render(request, 'medias/jeux/liste.html', {'jeux': jeux})

# Ajouter un jeu
def ajouter_jeu(request):
    form = JeuForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Jeu créé avec succès !")
    return render(request, 'ajouter_jeu.html',{'form': form})

# Ajouter un emprunt
class EmpruntCreateView(CreateView):
    model = Emprunt
    fields = ['membre', 'media', 'date_retour']
    template_name = 'emprunts/emprunt_form.html'
    success_url = reverse_lazy('emprunts_liste')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e.message)
            return self.form_invalid(form)

# Liste des emprunts via CBV
class EmpruntListView(ListView):
    model = Emprunt
    template_name = 'emprunts/emprunt_list.html'
    context_object_name = 'emprunts'

# Liste des emprunts via FBV
@login_required
def emprunt_liste(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'emprunts/liste.html', {'emprunts': emprunts})

# Ajouter un emprunt via FBV
@login_required
def emprunt_ajouter(request):
    form = EmpruntForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Emprunt ajouté avec succès !")
                return redirect('bibliothecaire:emprunts_liste')
            except ValidationError as e:
                form.add_error(None, e.message)
        else:
            messages.error(request, "Le formulaire contient des erreurs.")

    return render(request, 'emprunts/ajouter.html', {'form': form})

# Retourner un emprunt
@login_required
def retourner_emprunt(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, id=emprunt_id)

    today = timezone.now().date()

    if emprunt.date_retour > today:
        emprunt.date_retour = today
        emprunt.save()
        messages.success(request, "L'emprunt a été marqué comme retourné.")
    else:
        messages.info(request, "L'emprunt était déjà expiré ou retourné.")

    return redirect('bibliothecaire:emprunts_liste')
