from django.urls import path
from services import views


urlpatterns = [
    path('', views.ServicesView.as_view(), name='services'),
]
