from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("employees", views.employees, name="employees"),
    path("employee/<str:pk>", views.employee, name="employee"),
    path("", views.payments, name="payments"),
    path("payment/<str:pk>", views.payment, name="payment"),
    path("", views.pettys, name="pettys"),
    path("petty/<str:pk>", views.petty, name="petty"),
    
    path('create-employee', views.createEmployee, name="create-employee"),
    path('create-payment', views.createPayment, name="create-payment"),
    path('create-petty', views.createPetty, name="create-petty"),
    
    path('pdf-leave', views.pdf_leave, name="pdf-leave"),
    path('pdf-payment', views.pdf_payment, name="pdf-payment"),
    path('get_petty', views.get_petty, name="get_petty"),
    path('export-to-csv/', views.export_to_csv, name='export-to-csv'),
    path('export-to-petty/', views.export_to_petty, name='export-to-petty'),
    path('petty-to-excel/', views.petty_to_excel, name='petty-to-excel'),
    path('create/', views.create_leave_request, name='create_leave_request'),
    path('submit_leave_request/', views.submit_leave_request, name='submit_leave_request'),
    path('confirm_leave_request/<int:leave_request_id>/', views.confirm_leave_request, name='confirm_leave_request'),
    path('payment-to-excel/', views.payment_to_excel, name='payment-to-excel'),
    path('create-leave/', views.create_leave_request, name="create-leave"),
    path('leave_requests', views.leave_requests, name="leave-requests"),
    path('leave_req/', views.leave_req, name="leave_req"),
    path('submit-leave/', views.submit_leave_request, name="submit-leave"),
    path('confirm-leave/', views.confirm_leave_request, name="confirm-leave")
]