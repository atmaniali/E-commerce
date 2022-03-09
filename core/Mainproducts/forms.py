from pyexpat import model
from django import forms
from .models import Product,Categorie

class productForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at","categorie.created_at", "categorie.updated_at")
        
class categorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        exclude = ("created_at", "updated_at")        
        

