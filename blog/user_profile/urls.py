from django.urls import path,include
from .views import *


urlpatterns = [
    path('', ProfileView.as_view(), name='profile_detail_url'),
    path('<int:pk>/', ProfileView.as_view(), name='profile_detail_url'),
    path('update/', ProfileUpdate.as_view(), name='profile_update_url'),
    path('message/', include('mess.urls')),
]