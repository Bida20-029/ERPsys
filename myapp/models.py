from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Voucher(models.Model):
    ID_Num = models.IntegerField(primary_key=True, unique=True)
    Name = models.TextField(null=True, blank=True)
    Surname = models.TextField(null=True, blank=True)
    Contact = models.IntegerField()
    Voucher = models.CharField(max_length=20, null=True, blank=True)
    Cell_Amount = models.CharField(max_length=8, null=True, blank=True)
    Offer = models.CharField(max_length=8, null=True, blank=True)
    Voucher_Start = models.CharField(max_length=20, null=True, blank=True)
    Voucher_End = models.CharField(max_length=20, null=True, blank=True)
    Land_Board = models.TextField(max_length=30, default='NULL')
    Form = models.FileField(upload_to='pdfs/', blank=True, null=True)
    
class Loan(models.Model):
    Loan_ID = models.IntegerField(primary_key=True, unique=True)
    Name = models.TextField(null=True, blank=True)
    Surname = models.TextField(null=True, blank=True)
    Duration = models.IntegerField()
    LandBoard = models.TextField(null=True, blank=True)
    Principal = models.IntegerField()
    Start = models.CharField(max_length=15, null=True, blank=True)
    End = models.CharField(max_length=15, null=True, blank=True)
    Form = models.FileField(upload_to='pdfs/', blank=True, null=True)
    
from django.contrib.auth.models import User

class LeaveReques(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
        ]
    CONFIRMATION_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
        ]
    confirmation_status = models.CharField(max_length=1, choices=CONFIRMATION_CHOICES, default='P')
    requested_days = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    
class Member(models.Model): 
    ID_no = models.IntegerField(primary_key=True, unique=True)
    Name = models.TextField(null=True, blank=True)
    Surname = models.TextField(null=True, blank=True)
    LandBoard = models.TextField(null=True, blank=True)
    Contact = models.IntegerField()
    Residential_Address = models.CharField(max_length=15, null=True, blank=True)
    Form = models.FileField(upload_to='pdfs/', blank=True, null=True)




# Create your models here.
