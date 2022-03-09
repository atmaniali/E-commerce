from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name = "home"),
    path("create/", views.createProduct, name ="create-product"),
    path("create-categorie/", views.createCategorie, name ="create-categorie"),
    path("update/<int:productId>/", views.updateProduct, name = "update-product"),
    path("update-categorie/<int:categorieId>/", views.updateProduct, name = "update-categorie"),
    path("details/<int:productId>/", views.detailsProduct, name = "detail-product") ,
    path("details-categorie/<int:categorieId>/", views.detailsCategorie, name = "detail-categorie") ,
    path("delete/<int:productId>/", views.deleteProduct, name = "delete-product"),
    path("delete-categorie/<int:categorieId>/", views.deleteCategorie, name = "delete-categorie"),
]
