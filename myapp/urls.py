from django.urls import path
from . import views

from .views import PricingCalculatorView

urlpatterns = [
    path('', views.home, name='home'),
    path('manage-pricing/', views.manage_pricing_config, name='manage_pricing_config'),
    path('calculate-price/', PricingCalculatorView.as_view(), name='calculate_price'),
]
