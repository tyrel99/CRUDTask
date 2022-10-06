from django.shortcuts import render
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from .serializers import Customer_addrsSerializer, CustomerSerializer, Cust_bankSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import *


@csrf_exempt
def customer_api(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = CustomerSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'PUT':
        json_data = request.body              #The data in request body will be stored
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        cust = Customer_bankacc.objects.get(id=id)
        serializer = Cust_bankSerializer(cust, data = python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        cust = Customer_bankacc.objects.get(id=id)
        cust.delete()
        res = {'msg' : 'Data Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'applications/json')




class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerbankViewSet(viewsets.ModelViewSet):
    queryset = Customer_bankacc.objects.all()
    serializer_class = Cust_bankSerializer
    
class CustomerAddrsViewSet(viewsets.ModelViewSet):
    queryset = Customer_add.objects.all()
    serializer_class = Customer_addrsSerializer



# Create your views here.
