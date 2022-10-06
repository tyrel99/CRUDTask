from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(max_length = 100)
    #mob = serializers.IntegerField()
    
    #names = serializers.StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Customer
        fields = ['id','name','mob']

    
    def create(self,validate_data):
        return Customer.objects.create(**validate_data)


class Cust_bankSerializer(serializers.ModelSerializer):
    #acc_holder = serializers.ForeignKey(Customer, related_name = 'holder_name', on_delete = models.CASCADE)
    acc_no = serializers.IntegerField()
    branch = serializers.CharField(max_length = 100)



    acc_holder_name = serializers.CharField(source='acc_holder.name')
    
    class Meta:
        model = Customer_bankacc
        fields = ['id','acc_no','branch', 'acc_holder_name']

    def update(self, instance, validated_data):
        print(instance.acc_holder)
        instance.acc_holder = validated_data.get('acc_holder',instance.acc_holder)
        print(instance.acc_holder)
        instance.acc_no = validated_data.get('acc_no', instance.acc_no)
        instance.branch = validated_data.get('branch', instance.branch)
        #instance.acc_holder_name = validated_data.get('acc_holder_name', instance.acc_holder_name)
        
        instance.save()
        return instance

class Customer_addrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_add
        fields = ['add', 'city', 'state']

    
