from modulefinder import Module
from django.forms import ModelForm
from .models import Loan, Member, Voucher
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        
class cellForm(ModelForm):
    enctype="multipart/form-data"
    class Meta:
        model = Voucher
        fields= '__all__'
        
class loanForm(ModelForm):
    enctype="multipart/form-data"
    class Meta:
        model = Loan
        fields = '__all__'
        
class memberForm(ModelForm):
    enctype="multipart/form-data"
    class Meta:
        model = Member
        fields = '__all__'
        
       
        