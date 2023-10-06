from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import PricingConfig

# Create your tests here.
class PricingCalculatorAPITest(APITestCase):
    def setUp(self):
        self.pricing_config = PricingConfig.objects.create(
            tier='Standard',
            day='Monday',
            DBP=50.0,
            max_km_driven=19,
            DAP=2.0,
            TMF=1.5,
            WC=10.0,
            is_active=True
        )

    def test_calculate_price_endpoint(self):
        url = '/calculate-price/'
        data = {
            "tier": "Standard",
            "day": "Monday",
            "Tn": 1.5,
            "Dn": 10.0
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Price'], 62.25)  # Expected calculated price based on the given parameters
