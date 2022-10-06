from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','name','mob']

@admin.register(Customer_add)
class CustAdd(admin.ModelAdmin):
    list_display = ['add','city','state']


@admin.register(Customer_bankacc)
class CustAcc(admin.ModelAdmin):
    list_display = ['id','acc_holder','acc_no','branch']

