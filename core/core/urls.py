from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Mainproducts.urls")), # product app
    path("auth/", include("authentification.urls")),
]
