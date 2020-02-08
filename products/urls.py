from django.urls import path
from products.views import *


urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('<product_slug>/', ProductView.as_view(), name='product'),
]
