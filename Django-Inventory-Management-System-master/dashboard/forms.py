from django import forms
from .models import Product, Historique, Maintenance


CATEGORY = (
    ('', 'Choisir une catégorie'),
    ('à feux de signalisation', 'Carrefours à feux de signalisation'),
    ('ronds-points', 'Carrefours ronds-points'),
    ('en T', 'Carrefours en T'),
    ('en croix', 'Carrefours en croix'),
    ('giratoires', 'Carrefours giratoires'),
    ('non réglementés', 'Carrefours non réglementés'),
    ('à sens unique', 'Carrefours à sens unique'),
    ('à sens multiple', 'Carrefours à sens multiple'),
    ('en étoile', 'Carrefours en étoile'),
    ('avec passages piétons', 'Carrefours avec passages piétons'),
)

class ProductForm(forms.ModelForm):
    name  = forms.CharField(label='Nom du Carrefour')
    quantity  = forms.IntegerField(label="Densité de Traffic")
    # category   = forms.CharField(label="Catégorie")
    category = forms.ChoiceField(label='Catégorie', choices=CATEGORY, required=False)
    class Meta:
        model = Product
        fields = ['category','name', 'quantity']

class HistoryForm(forms.ModelForm):
    panne  = forms.CharField(label='Panne')
    ti  = forms.IntegerField(label="Temps d'indisponibilité(h)")
    ttr   = forms.IntegerField(label="Temps total de reparation (h)")
    
    class Meta:
        model = Historique
        fields = '__all__'

class MaintenanceForm(forms.ModelForm):
    observations   = forms.CharField(label="Observations", initial="X")
    class Meta:
        model = Maintenance
        fields = '__all__'


#class OrderForm(forms.ModelForm):

 #   fields = '__all__'
 # class Meta:
  #      model = Order
   #     fields = ['name', 'order_quantity']
