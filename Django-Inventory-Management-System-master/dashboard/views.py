from django.shortcuts import render, redirect, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Product, Historique, Maintenance
from .forms import ProductForm, HistoryForm, MaintenanceForm 
from django.shortcuts import get_object_or_404 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from datetime import date, timedelta
from django.db.models import Sum
from django.shortcuts import render, HttpResponseRedirect
from django.http import FileResponse
from django.conf import settings
from django.http import JsonResponse
from django.views import View
import os
from django.http import HttpResponse
from .Analyser import traitement_formulaire as form_treatment
import logging

#from .forms import OrderForm
# Create your views here.

@login_required(login_url='login')
@csrf_exempt
def HomePage(request):
    deux_jours_plus_tard = date.today() + timedelta(days=2)
    maint_rouge = Maintenance.objects.filter(date__lt =deux_jours_plus_tard)

    today = date.today()
    start_date = today + timedelta(days=7) 
    end_date = today + timedelta(days=2)
    maint_orange  = Maintenance.objects.filter(date__gte=end_date, date__lt=start_date)
    
    produits_rouge = Product.objects.filter(quantity__lt = 3)
    produits_orange = Product.objects.filter(quantity__range=[3, 10])
    produits_vert = Product.objects.filter(quantity__gt=10)
    context = {
        'produits_rouge': produits_rouge,
        'produits_orange': produits_orange,
        'produits_vert': produits_vert,
        'maint_rouge': maint_rouge,
        'maint_orange': maint_orange,
    }
    return render(request, 'index.html', context)

@csrf_exempt
def login_admin(request):
    # Vue pour le login de l'administrateur
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')

        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect('adminlogin')
        else:
            return HttpResponse("Le nom d'utilisateur ou le mot de passe est incorrect")


    return render(request,'admin_login.html')

@csrf_exempt
def loginadmin(request):
    # Vue pour le login de l'administrateur
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')

        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect('admin/login/')
        else:
            return HttpResponse("Username and password is incorrect")


    return render(request,'admin_login.html') 

@csrf_exempt
def role_selection(request):
    return render(request, 'role_selection.html')

@csrf_exempt
def a_propos(request):
    return render(request,'about.html')

@csrf_exempt
def contact(request):
    return render(request,'contact.html')

@csrf_exempt
def produits(request):
    return render(request,'products.html')


@csrf_exempt
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')

        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username and password is incorrect")


    return render(request,'login.html')

@csrf_exempt
def LogoutPage(request):
    logout(request)
    return redirect('login')

@csrf_exempt
@login_required(login_url='user-login')
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    #order = Order.objects.all()
    #order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'form': form,
        #'order': order,
        'product': product,
        'product_count': product_count,
        #'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
@csrf_exempt
def products(request):
    product = Product.objects.all()
    product_count = product.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    #order = Order.objects.all()
    #order_count = order.count()
    product_quantity = Product.objects.filter(name='')
    produits_rouge = Product.objects.filter(quantity__lt = 3)
    produits_orange = Product.objects.filter(quantity__range=[3, 9])
    produits_vert = Product.objects.filter(quantity__gte=10)
    rouge_count = produits_rouge.count()
    orange_count = produits_orange.count()
    vert_count = produits_vert.count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'produits_rouge': produits_rouge,
        'produits_orange': produits_orange,
        'produits_vert': produits_vert,
        'rouge_count': rouge_count,
        'orange_count': orange_count,
        'vert_count': vert_count,
        #'order_count': order_count,

    }
    return render(request, 'dashboard/products.html', context)


@login_required(login_url='user-login')
@csrf_exempt
def product_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/products_detail.html', context)


@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def customers(request):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    #order = Order.objects.all()
    #order_count = order.count()
    context = {
        'customer': customer,
        'customer_count': customer_count,
        'product_count': product_count,
        #'order_count': order_count,
    }
    return render(request, 'dashboard/customers.html', context)


@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def customer_detail(request, pk):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    #order = Order.objects.all()
    #order_count = order.count()
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
        'customer_count': customer_count,
        'product_count': product_count,
        #'order_count': order_count,

    }
    return render(request, 'dashboard/customers_detail.html', context)


@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def product_edit(request, pk):
    if request.method == 'POST':
        pi = Product.objects.get(id=pk)
        fm = ProductForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Product.objects.get(id=pk)
        fm = ProductForm(instance=pi)

    return render(request, 'dashboard/products_edit.html', {'form': fm})

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def product_edit_home(request, pk):
    if request.method == 'POST':
        pi = Product.objects.get(id=pk)
        fm = ProductForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Product.objects.get(id=pk)
        fm = ProductForm(instance=pi)

    return render(request, 'dashboard/products_edit_home.html', {'form': fm})

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def maintenance_edit(request, pk):
    if request.method == 'POST':
        pi = Maintenance.objects.get(id=pk)
        fm = MaintenanceForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Maintenance.objects.get(id=pk)
        fm = MaintenanceForm(instance=pi)

    return render(request, 'maintenance_edit.html', {'form': fm})

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def maintenance_edit_home(request, pk):
    if request.method == 'POST':
        pi = Maintenance.objects.get(id=pk)
        fm = MaintenanceForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Maintenance.objects.get(id=pk)
        fm = MaintenanceForm(instance=pi)

    return render(request, 'maintenance_edit_home.html', {'form': fm})

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def historique_edit(request, pk):
    if request.method == 'POST':
        pi = Historique.objects.get(id=pk)
        fm = HistoryForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Historique.objects.get(id=pk)
        fm = HistoryForm(instance=pi)

    return render(request, 'historique_edit.html', {'form': fm})

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def ajouter_stock(request, produit_id):
    if request.method == 'POST':
        produit = get_object_or_404(Product, pk=produit_id)
        qte = int(request.POST['quantite'])
        produit.quantity += qte
        produit.save()
        
    else:
        produit = get_object_or_404(Product, pk=produit_id)
        
    return render(request, 'dashboard/ajout_produits.html')

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def ajouter_stock_home(request, produit_id):
    if request.method == 'POST':
        produit = get_object_or_404(Product, pk=produit_id)
        qte = int(request.POST['quantite'])
        produit.quantity += qte
        produit.save()
        
    else:
        produit = get_object_or_404(Product, pk=produit_id)
        
    return render(request, 'dashboard/ajout_prod_home.html')

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def retirer_stock(request, produit_id):
    if request.method == 'POST':
        produit = get_object_or_404(Product, pk=produit_id)
        qte = int(request.POST['quantite'])
        produit.quantity -= qte
        produit.save()
        
    else:
        produit = get_object_or_404(Product, pk=produit_id)
        
    return render(request, 'dashboard/sortie_stock.html')

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def retirer_stock_home(request, produit_id):
    if request.method == 'POST':
        produit = get_object_or_404(Product, pk=produit_id)
        qte = int(request.POST['quantite'])
        produit.quantity -= qte
        produit.save()
        
    else:
        produit = get_object_or_404(Product, pk=produit_id)
        
    return render(request, 'dashboard/sortie_stock_home.html')

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])  
@csrf_exempt  
def ajout_stock(request):
    return render(request, 'dashboard/ajout_produits.html')
    


@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def history_delete(request, pk):
    item = Historique.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('history')
    context = {
        'item': item
    }
    return render(request, 'historique.html', context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def maintenance_delete(request, pk):
    item = Maintenance.objects.get(id=pk) 
    if request.method == 'POST':
        item.delete()
        return redirect('maintenance')
    context = {
        'item': item,
    }
    return render(request, 'maintenance.html', context)

def alertes_peremption(request):
       produits_proches_peremption = Product.objects.filter(est_proche_peremption=True)
       return render(request, 'alertes_peremption.html', {'produits': produits_proches_peremption})


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
@csrf_exempt
def modif(request, product_id):
    return render(request, 'modif.html', {'product_id': product_id})


@login_required(login_url='user-login')
@csrf_exempt
def history(request):
    history = Historique.objects.all()
    history_count = history.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    total_ti = Historique.objects.aggregate(Sum('ti'))
    total_ttr = Historique.objects.aggregate(Sum('ttr')) 

    som_ti=total_ti['ti__sum']
    som_ttr=total_ttr['ttr__sum']
    


    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            form.save()
            panne_name = form.cleaned_data.get('panne')
            messages.success(request, f'{panne_name} a bien été ajouté')
            return redirect('history')
    else:
        form = HistoryForm()
    context = {
        'history': history,
        'form': form,
        'customer_count': customer_count,
        'history_count': history_count,
        'total_ti' : som_ti,
        'total_ttr' : som_ttr,
        
        #'order_count': order_count,
    }
    return render(request, 'historique.html', context)


@login_required(login_url='user-login')
@csrf_exempt
def maintenance(request):
    maint = Maintenance.objects.all()
    #maintenance_date = maint.date.date()
    maint_count = maint.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    

    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            operation_name = form.cleaned_data.get('operation')
            messages.success(request, f'l opération {operation_name} a bien été ajoutée')
            return redirect('maintenance')
    else:
        form = MaintenanceForm()
    context = {
        'maint': maint,
        'form': form,
        'customer_count': customer_count,
        'maint_count': maint_count,
        #'maint_date': maintenance_date,
        
    }
    return render(request, 'maintenance.html', context)

@csrf_exempt
def view_pdf(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'memoire', 'memoire pat.pdf')
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')

@csrf_exempt
def itineraire(request):
    # Logique de la vue pour générer la page de destination
    return render(request, 'itineraire.html')

@csrf_exempt
def traitement_formulaire(request):
        # Appeler la fonction importée
        result = form_treatment(request)
        # Faire quelque chose avec le résultat
        return HttpResponse(result)

# def traitement_formulaire(request):
#     if request.method == 'POST':
#         lieu_depart = request.POST.get('lieu-depart')
#         destination = request.POST.get('destination')
#         heure_depart = request.POST.get('heure-depart')

#         # Faites ici ce que vous souhaitez faire avec les données, par exemple les enregistrer dans la base de données
#         # ou effectuer des calculs avec les valeurs

#         return HttpResponse("Données du formulaire reçues et traitées avec succès !")
