from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=30)
    roll_no=models.CharField(max_length=8)
    reg_no=models.IntegerField(max_length=20)
    parents_mail_1=models.EmailField(unique=True,null=False,blank=False,max_length=254)
    parents_mail_2=models.EmailField(unique=True,null=False,blank=False,max_length=254)
    is_inside=models.BooleanField(default=True)