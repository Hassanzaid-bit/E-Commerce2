from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/braintree', views.braintree_payment_process, name='braintree_process'),
    path('process/mpesa', views.mpesa_payment_process, name='mpesa_process'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
] 