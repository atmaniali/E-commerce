from django.db import models

# Create your models here.
class Categorie(models.Model):
    name_category = models.CharField(max_length=200)
    created_at    = models.DateTimeField(auto_now_add= True)
    updated_at    = models.DateTimeField(auto_now = True)
    
    def __str__(self) -> str:
        return f"categorie {self.name_category}"
    
class Product(models.Model):
    name       = models.CharField(max_length=200)
    label      = models.TextField()
    prix       = models.DecimalField(max_digits=10,decimal_places=2)
    quanities  = models.IntegerField()
    categorie  = models.ForeignKey(Categorie, on_delete= models.CASCADE, related_name= "products")
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self) -> str:
        return f"product : {self.name} - prix {self.prix} $"

 