from django.urls import path
from . import views
from cart import views as cart_views

app_name = 'computers'

urlpatterns = [
    path("", views.home, name='home'), 
    path("computers", views.computers, name='systems'),
    path("products", views.products, name='products'),
    path('products/<int:pk>', views.product_details, name="product-details"),
    path("payment", views.payment, name="payment"),
    path("sell/", views.computer_upload_view, name='sell')
]
