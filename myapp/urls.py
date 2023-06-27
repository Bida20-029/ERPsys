from django import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("main", views.main, name='main'),
    # path('loginhome/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='loginhome/'),
    path("myapp/<str:pk>", views.myapp, name="myapp"),
    path("", views.loans, name="loans"),
    path("", views.members, name="members"),
    path("member/<str:pk>", views.member, name="member"),
    path("", views.vouchers, name="vouchers"),
    path("voucher/<str:pk>", views.voucher, name="voucher"),
    
    path('create-loan', views.createLoan, name="create-loan"),
    path('create-member', views.createMember, name="create-member"),
    path('create-voucher', views.createVoucher, name="create-voucher"),
    path('Vouchers-Page', views.VouchersPage, name='Vouchers-Page'),
    path('login/', views.login, name='login'),
    # path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('register/', views.register, name='register'),
    path('Loans-Page', views.LoansPage, name='Loans-Page'),
    path('Members-Page', views.MembersPage, name='Members-Page'),
    path('Home-Page', views.home, name='Home-Page'),
    path('vouchers/<int:pk>/', views.get_voucher, name='get_voucher'),
    
    path('pdf-view/', views.pdf_view, name='pdf-view'),
    path('pdf-loan/', views.pdf_loan, name='pdf-loan'),
    path('pdf-member/', views.pdf_member, name='pdf-member'),
    path('voucher-to-csv/', views.voucher_to_csv, name='voucher-to-csv'),
    path('loan-to-csv/', views.loan_to_csv, name='loan-to-csv'),
    path('voucher-to-excel/', views.voucher_to_excel, name='voucher-to-excel'),
    path('loan-to-excel/', views.loan_to_excel, name='loan-to-excel'),
    path('loginhome/', views.loginPage, name='loginhome/'),
    path('registerhome/', views.registerPage, name='registerhome/'),
    path('logouthome/', views.logoutUser, name='logout'),
    path('about/', views.about, name='about')
]