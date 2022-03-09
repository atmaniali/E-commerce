from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product,Categorie
from .forms import productForm, categorieForm

# Create your views here.

# home page
def index(request):
    category = request.GET.get("categorie")
    if category == None:
        product = Product.objects.all()
    else: 
        product = Product.objects.filter(categorie__name_category = category)
             
    categories = Categorie.objects.all()
    
    context = {"products" : product, 
               "categories" : categories,
               }
    return render(request, "Mainproducts/index.html", context)

# product crud

def createProduct(request):
    """ create new product """
    
    form = productForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(form)
        return redirect("home")
    return render(request, "Mainproducts/create-product.html", {"form":form ,"name": "Create"}) 

def updateProduct(request, productId):
    """ modifie a product by id given """
    
    obj_product = get_object_or_404(Product, pk=productId)
    form = productForm(request.POST or None, instance= obj_product)
    if form.is_valid():
        form.save()
        print(form)
        return redirect("home")
    return render(request, "Mainproducts/create-product.html", {"form":form, "name": "Update"}) 

def detailsProduct(request, productId):
    """ details of a product by @productId given """
    
    obj_product = get_object_or_404(Product, pk=productId)
    return render(request, "Mainproducts/detail-product.html", {"product":obj_product}) 

def deleteProduct(request, productId):
    """ delete of a product by @productId given """
    
    obj_product = get_object_or_404(Product, pk=productId)
    obj_product.delete()
    return redirect("home")

# categorie crud

def createCategorie(request):
    """ create a new categorie """
    
    form = categorieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "Mainproducts/create-categorie.html", {"form" : form}) 

def updateCategorie(request, categorieId):
    """ update of a categorie by @categorieId given """
    
    obj_categorie = get_object_or_404(Categorie, pk=categorieId)
    form = categorieForm(request.POST or None, instance= obj_categorie)
    if form.is_valid():
        form.save()
        print(form)
        return redirect("home")
    return render(request, "Mainproducts/create-categorie.html", {"form":form}) 

def detailsCategorie(request, categorieId):
    """ details of a categorie by @categorieId given """
    
    obj_categorie = get_object_or_404(Categorie, pk=categorieId)
    return render(request, "Mainproducts/detail-categorie.html", {"categorie":obj_categorie}) 

def deleteCategorie(request, categorieId):
    """ delete of a categorie by @categorieId given """
    
    Categorie.objects.get(id = categorieId).delete()
    return redirect("home")

