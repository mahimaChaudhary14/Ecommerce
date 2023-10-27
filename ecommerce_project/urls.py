"""
URL configuration for ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Dashboard, name='dashboard'),
    path('add_products/', views.add_product, name='add_products'),
    path('view_products/', views.view_product, name='view_products'),

    path('edit_products/<str:id>', views.edit_product, name='edit_products'),
    path('update_products/', views.update_product, name='update_products'),
    path('delete_products/<str:id>', views.delete_product, name='delete_products'),



    


]
