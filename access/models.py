from django.db import models
import uuid 
from django.contrib.auth.models import User
from django.conf import settings

class Approval(models.Model):
    email = models.EmailField()
    Message = models.TextField(null=True, blank=True)
    Approval = models.BooleanField(default=True)
    

class Employee(models.Model):
    id = models.CharField(primary_key=True, default=1, max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    Name = models.TextField(null=True, blank=True)
    Surname = models.TextField(null=True, blank=True)
    leavedays_requested = models.IntegerField()
    available_leave_days = models.PositiveIntegerField(default=30)
    
    
class Payment(models.Model):
    Voucher_ID = models.IntegerField(primary_key=True, unique=True)
    PVNumber = models.IntegerField(default=0)
    Paid_To = models.CharField(max_length=30)
    Prepared_By = models.TextField(null=True, blank=True)
    Funds_use_breakdown = models.TextField(null=True, blank=True)
    Amount_in_words = models.TextField(null=True, blank=True)
    Amount = models.DecimalField(null=True, decimal_places=2, max_digits=20)
    Date = models.CharField(max_length=10)
    Approval_Signature_1 = models.FileField(upload_to='pdfs/', blank=True)
    Approval_Signature_2 = models.FileField(upload_to='pdfs/', blank=True)
    Attachments = models.FileField(upload_to='pdfs/', blank=True, null=True)
    Comments = models.CharField(max_length=100)

class Petty(models.Model):
    Petty_ID = models.IntegerField(primary_key=True, unique=True)
    Date = models.CharField(max_length=15, null=True, blank=True)
    Receipt = models.FileField(upload_to='pdfs/', blank=True, null=True)
    Cash_Used_For = models.TextField(null=True, blank=True)
    Total_Price = models.CharField(max_length=15, null=True, blank=True)
    Petty_Cash_Taken = models.CharField(max_length=15, null=True, blank=True)
    Petty_Cash_Used = models.CharField(max_length=15, null=True, blank=True)
    Balance = models.CharField(max_length=15, null=True, blank=True)
    Balance_cd = models.CharField(max_length=15, null=True, blank=True)
    Filled_In_By = models.TextField(null=True, blank=True) 
    Approval_Signature_1 = models.FileField(upload_to='pdfs/', blank=True, null=True)
    Approval_Signature_2 = models.FileField(upload_to='pdfs/', blank=True, null=True)
    Comments = models.CharField(max_length=100)
    
class LeaveRequest(models.Model):
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
    leave_request_id = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmation_status = models.CharField(max_length=1, choices=CONFIRMATION_CHOICES, blank=True)
    requested_days = models.PositiveIntegerField(default=0)
    available_leave_days = models.IntegerField(default=30)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.user.username} - {self.start_date} to {self.end_date}"



# Create your models here.
