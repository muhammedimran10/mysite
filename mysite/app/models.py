from django.db import models
# from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Memmber(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.PROTECT)
    fullname= models.CharField(max_length=50)
    address1= models.CharField(max_length=50)
    address2= models.CharField(max_length=50)
    address3= models.CharField(max_length=50)
    mobile_no= models.CharField(max_length=25)
    active= models.BooleanField(default=True)
    profile_pic = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.fullname


class Weekly_entry(models.Model):
    entry_date= models.DateField(timezone.now())
    memmber_id= models.ForeignKey(Memmber,on_delete=models.PROTECT)
    invest_amt= models.IntegerField()
    loan_amt= models.IntegerField()
    remarks= models.CharField(max_length=50,blank=True)

class Loan(models.Model):
    loan_date= models.DateField(timezone.now())
    memmber_id= models.ForeignKey(Memmber,on_delete=models.PROTECT)
    loan_amt= models.IntegerField()
    remarks= models.CharField(max_length=50,blank=True)

class Loan_interest(models.Model):
    date = models.DateField(timezone.now())
    memmber_id = models.ForeignKey(Memmber,on_delete=models.PROTECT)
    interest_amt = models.IntegerField()
