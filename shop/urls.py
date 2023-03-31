"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('detail/<int:id>', detail, name='detail'),
    path('favorites/<int:id>', favorites, name='favorites'),
    path('favpage/', favorites_page, name='favpage'),
    path('delete/<int:id>', remove_from_favpage, name='delete'),
    path('cart/<int:id>', cart, name='cart'),
    path('cartpage/', cart_page, name='cartpage'),
    path('deleete/<int:id>', remove_from_cartpage, name='deleete'),
    path('aboutus/', about_us, name='info'), 
    path('auth/', auth, name='auth')
]

urlpatterns += static(
    MEDIA_URL, document_root=MEDIA_ROOT
)