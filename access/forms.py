from modulefinder import Module
from django.forms import ModelForm
from .models import  Payment, Petty, Employee, Approval
from .models import LeaveRequest
from django import forms

class LeaveRequestForm(ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['leave_request_id', 'requested_days', 'start_date', 'end_date', 'reason', 'confirmation_status']
        widgets = {
            'confirmation_status': forms.HiddenInput(),
        }

class leaveForm(ModelForm):
    enctype="multipart/form-data"
    class Meta:
        model = Employee
        fields = '__all__'
        
class paymentForm(ModelForm):
    enctype="multipart/form-data"
    class Meta:
        model = Payment
        fields = ['Voucher_ID', 'PVNumber', 'Paid_To', 'Prepared_By', 'Funds_use_breakdown', 'Amount_in_words', 'Amount', 'Date', 'Attachments']
        
class pettyForm(ModelForm):
    enctype="multipart/form-data"
    class Meta:
        model = Petty
        fields = ['Petty_ID', 'Date', 'Receipt', 'Cash_Used_For', 'Total_Price', 'Petty_Cash_Taken', 'Petty_Cash_Used', 'Balance', 'Balance_cd', 'Filled_In_By']

class ApprovalForm(ModelForm):
    enctype="multipart/form-data"
    class Meta:
        model = Approval
        fields = '__all__'
       
    