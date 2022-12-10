from django.shortcuts import render
from django.http import HttpResponseRedirect

from .regex import Regex
from .forms import Formulaire_inscription

def inscription_form(request):
    if request.method == 'POST':
        form = Formulaire_inscription(request.POST)
        if form.is_valid() and Regex.verif_mail(form.cleaned_data['mail']) and Regex.verif_tel(form.cleaned_data['telephone']) and Regex.verif_cp(form.cleaned_data['code_postal']):#REMPLACER LES NOMS ENTRE GUILLEMETS PAR LES NOMS DES CASES DU FORMULAIRE 
            reussi = "réussi"
            return render(request, 'inscription/inscription_form.html', {'form' : form, 'reussi' : reussi})
        else:
            erreur_mail = ""
            erreur_tel = ""
            erreur_cp = ""

            if not Regex.verif_mail(form.cleaned_data['mail']):#REMPLACER LES NOMS ENTRE GUILLEMETS PAR LES NOMS DES CASES DU FORMULAIRE 
                erreur_mail = "Mauvais format d'adresse mail"
            if not Regex.verif_tel(form.cleaned_data['telephone']):
                erreur_tel = "Mauvais format de numéro de téléphone : les chiffres doivent être séparés par des points, des tirets ou des espaces"
            if not Regex.verif_cp(form.cleaned_data['code_postal']):
                erreur_cp = "Mauvais format de code postal"
            context = {
                'form' : form,
                'erreur_mail' : erreur_mail,
                'erreur_tel' : erreur_tel,
                'erreur_cp' : erreur_cp
            }
            return render(request, 'inscription/inscription_form.html', context)
    else:
        form = Formulaire_inscription()
    
    return render(request, 'inscription/inscription_form.html', {'form' : form})