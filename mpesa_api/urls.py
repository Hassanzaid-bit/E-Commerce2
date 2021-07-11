from django.urls import path
from . import views

app_name = "mpesa"

urlpatterns = [
  #  path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa, name='lipa_na_mpesa')
]