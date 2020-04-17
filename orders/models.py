from django.db import models

# Create your models here.

class Order(models.Model):
    # Orders.
    firts_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document =  models.CharField(max_length=8, unique=True)
    cuil = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    order = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    date_order = models.DateTimeField(auto_now_add=True)
    # Deliver.
    state = models.BooleanField(blank=True, null=True)
    observation = models.TextField(max_length=200,blank=True, null=True)
    date_deliver = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return '{} {}, DNI: {}, Cuil: {}'.format(self.firts_name,self.last_name,self.document,self.cuil)
    
