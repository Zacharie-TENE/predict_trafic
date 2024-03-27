from django.urls import path
from . import views
import logging


urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    #path('home/',views.HomePage,name='home'),
    path('products/', views.products, name='dashboard-products'),
    path('products/delete/<int:pk>/', views.product_delete,
         name='dashboard-products-delete'),

     path('history/delete/<int:pk>/', views.history_delete,
         name='history-delete'),

     path('maintenance/delete/<int:pk>/', views.maintenance_delete,
         name='maintenance-delete'),
    path('products/detail/<int:pk>/', views.product_detail,
         name='dashboard-products-detail'),
    path('products/edit/<int:pk>/', views.product_edit,
         name='dashboard-products-edit'),

    path('products/editHome/<int:pk>/', views.product_edit_home,
         name='products-edit-home'),

     path('historique/edit/<int:pk>/', views.historique_edit,
         name='historique-edit'),

     path('maintenance/edit/<int:pk>/', views.maintenance_edit,
         name='maintenance-edit'),

    path('maintenance/editHome/<int:pk>/', views.maintenance_edit_home,
         name='maintenance-edit-home'),
    path('customers/', views.customers, name='dashboard-customers'),
    path('customers/detial/<int:pk>/', views.customer_detail,
         name='dashboard-customer-detail'),
     #path('ajout_stock/', views.ajout_stock, name='ajout_stock'),

     path('products/modif/<int:produit_id>/', views.modif, name='modif'),
     
path('products/ajout/<int:produit_id>/', views.ajouter_stock, name='ajouter_stock'),
path('products/ajoutHome/<int:produit_id>/', views.ajouter_stock_home, name='ajouter_stock_home'),
path('products/retrait/<int:produit_id>/', views.retirer_stock, name='retirer_stock'),
path('products/retraitHome/<int:produit_id>/', views.retirer_stock_home, name='retirer_stock_home'),
path('history/', views.history, name='history'),
path('maintenance/', views.maintenance, name='maintenance'),
path('memoire/', views.view_pdf, name='view_pdf'),
    #path('order/', views.order, name='dashboard-order'),

    path('itineraire/', views.itineraire, name='itineraire'),
    path('traitement_formulaire/', views.traitement_formulaire, name='traitement_formulaire'),


]
