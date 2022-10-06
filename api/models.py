from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length = 100)
    mob = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Customer_add(models.Model):
    add = models.ForeignKey(Customer,on_delete = models.CASCADE)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)

    #def __str__(self):
    #    return str(self.city)



class Customer_bankacc(models.Model):
    acc_holder = models.ForeignKey(Customer, related_name = 'holder_name', on_delete = models.CASCADE)
    acc_no = models.IntegerField()
    branch = models.CharField(max_length = 100)


    # def __str__(self):
    #     return str(self.branch)

    




# Create your models here.
