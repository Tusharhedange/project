from django.db import models

# Create your models here.
class Seller(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=13)
    password=models.CharField(max_length=20,null=True,blank=True)
    pic=models.FileField(upload_to='seller profile',default='#')

    def __str__(self):
        return self.name
       



class Product(models.Model):
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    des=models.TextField()
    price=models.FloatField()
    quantity=models.IntegerField(default=0)
    discount=models.IntegerField()
    pic=models.FileField(upload_to='Product',default='koala.jpg')
    discountedprice=models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name