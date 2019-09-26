from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>', ProfileView.as_view(), name='profile_detail_url'),
]