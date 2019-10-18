from django.urls import path
from .views import *


urlpatterns = [
     path('', MessageCreate.as_view(), name='mess_create_url'),
     path('<int:pk>/', MessageCreate.as_view(), name='mess_create_url'),
]