from django.db import models

# Create your models here.
class User(models.Model):
    mail = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self) -> str:
        return f"Name is : {self.name} , Mail is : {self.mail}"

class Subcategory(models.Model):
    name = models.CharField(max_length=20)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class Transaction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.ForeignKey(Subcategory,on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=20,decimal_places=4)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=100)


