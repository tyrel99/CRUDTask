"""CBA URL Configuration

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
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# Registered Customerviewset with routers
router.register('customer', views.CustomerViewSet, basename = 'customer')
router.register('custacc', views.CustomerbankViewSet, basename = 'custacc')
router.register('custadd', views.CustomerAddrsViewSet, basename = 'custadd')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Custapi/',views.customer_api),
    path('', include(router.urls)),


]
