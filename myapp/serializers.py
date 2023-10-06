from rest_framework import serializers
from .models import PricingConfig

class PricingCalculatorSerializer(serializers.Serializer):
    tier = serializers.ChoiceField(choices=PricingConfig.TIER_CHOICES)
    day = serializers.ChoiceField(choices=PricingConfig.DAY_CHOICES)
    Tn = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    Dn = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
