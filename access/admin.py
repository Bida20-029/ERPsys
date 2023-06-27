from django.contrib import admin
from .models import Payment, Petty, Employee, Approval, LeaveRequest
from django.urls import reverse
from django.utils.html import format_html


admin.site.register(Employee)
admin.site.register(Approval)

class PaymentAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = [field.name for field in self.model._meta.fields]  # Get all field names from the model
        
        if obj and not obj.Approval_Signature_1:
            readonly_fields.remove('Approval_Signature_1')
        if obj and not obj.Approval_Signature_2:
            readonly_fields.remove('Approval_Signature_2')
        if obj and not obj.Comments:
            readonly_fields.remove('Comments')
        
        return readonly_fields

admin.site.register(Payment, PaymentAdmin)

class PettyAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = [field.name for field in self.model._meta.fields]  # Get all field names from the model
        
        if obj and not obj.Comments:
            readonly_fields.remove('Comments')
        if obj and not obj.Approval_Signature_1:
            readonly_fields.remove('Approval_Signature_1')
        if obj and not obj.Approval_Signature_2:
            readonly_fields.remove('Approval_Signature_2')
        
        return readonly_fields

admin.site.register(Petty, PettyAdmin)
# Register your models here.

class LeaveRequestAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = [field.name for field in self.model._meta.fields]  # Get all field names from the model
        
        if obj and not obj.confirmation_status:
            readonly_fields.remove('confirmation_status')
        if obj and not obj.status:
            readonly_fields.remove('status')
        
        return readonly_fields

admin.site.register(LeaveRequest, LeaveRequestAdmin)
