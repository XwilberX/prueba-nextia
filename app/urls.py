from django.urls import path
from .views import ListUserView, login, register, BienesListView

app_name = 'user'

urlpatterns = [
    path('users/', ListUserView.as_view(), name='users'),
    path('auth/login/', login, name='auth'),
    path('auth/register/', register, name='register'),
    path('bienes/', BienesListView.as_view(), name='bienes'),
]
