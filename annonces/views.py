from .forms import CategoryForm, AnnonceForm
from .models import Annonce, Category
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# def valides_annonces(request):
#     valides_annonces = Annonce.objects.filter(statut = 'valide')
#     response = "list of annonces title <br>"
#     for i in valides_annonces:
#         response += f"{i.titre} <br>"

#     return HttpResponse(response)

def annonces(request):
    annonces = Annonce.objects.all()
    return render(request, 'liste_annonces.html', {'annonces':annonces})
# @login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = Category.objects.filter(name = name)
            if category:
                return render(request, 'add_category.html', {'exist':'category already exist'})
            else:
                form.save()
                return render(request, 'add_category.html', {'message':'category added successfully'})
        else:
            return render(request, 'add_category.html', {'form':form})
    else:
        form = CategoryForm()
        return render(request, 'add_category.html', {'form':form})
@login_required
def add_annonce(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = AnnonceForm(request.POST, request.FILES)
        category_id = request.POST.get('category')
        if form.is_valid() and category_id:
            annonce = form.save()
            annonce.category = Category.objects.get(id=category_id)
            annonce.save()
            return render(request, 'add_annonce.html', {'form': AnnonceForm(), 'categories': categories, 'message': 'Annonce added successfully'})
        else:
            return render(request, 'add_annonce.html', {'form': form, 'categories': categories})
    else:
        form = AnnonceForm()
        return render(request, 'add_annonce.html', {'form': form, 'categories': categories})


