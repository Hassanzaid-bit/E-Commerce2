from django.urls import path
from . import views

app_name = 'components'

urlpatterns = [
    path("", views.components, name='components')
]