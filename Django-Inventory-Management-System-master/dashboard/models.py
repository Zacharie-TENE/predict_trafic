from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
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


class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    date_peremption   = models.DateTimeField(null=True)

    def est_proche_peremption(self):
           return self.date_peremption - timezone.now().date() <= timezone.timedelta(days=3)

    def __str__(self):
        return f'{self.name}'
    

EXECUTANT = (
    ('Mecanicien', 'Mecanicien'),
    ('Chauffeur', 'Chauffeur'),
    ('Electricien', 'Electricien'),
)

FREQUENCE = (
    ('Journalier', 'Journalier'),
    ('Hebdomadaire', 'Hebdomadaire'),
    ('Mensuel', 'Mensuel'),
    ('Trimestriel', 'Trimestriel'),
    ('Semestriel', 'Semestriel'),
    ('Annuel', 'Annuel'),
)

class Maintenance(models.Model):
    operation  = models.CharField(max_length= 700, null=True)
    executant = models.CharField(max_length=50, choices=EXECUTANT, null=True)
    frequence = models.CharField(max_length=50, choices=FREQUENCE, null=True)
    observations = models.CharField(max_length= 700, null=True)
    date= models.DateTimeField()



class QHSE(models.Model):
    Nom_licence  = models.CharField(max_length= 70)
    date_exp   = models.DateTimeField()

    
class Membre(models.Model):
    nom  = models.CharField(max_length= 70)
    grade  = models.CharField(max_length= 100)    

class Historique(models.Model):
    panne  = models.CharField(max_length= 255)
    ti  = models.PositiveIntegerField(null=True)
    ttr   = models.PositiveIntegerField(null=True)
    date  = models.DateTimeField()
    
    #total = models.ForeignKey(Total, null=True, on_delete= models.SET_NULL)
    #maintenance = models.ForeignKey(Maintenance, null=True, on_delete= models.SET_NULL)
    #qhse = models.ForeignKey(QHSE, null=True, on_delete= models.SET_NULL)
    #membre = models.ForeignKey(Membre, null=True, on_delete= models.SET_NULL)



#class Order(models.Model):
#    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#    order_quantity = models.PositiveIntegerField(null=True)

#    def __str__(self):
#        return f'{self.customer}-{self.name}'
