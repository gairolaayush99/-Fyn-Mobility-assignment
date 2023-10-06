from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .forms import PricingConfigForm
from .models import PricingConfig
from .serializers import PricingCalculatorSerializer
from rest_framework.views import APIView
from django.utils import timezone

from loguru import logger

def home(request):
    return HttpResponse("Hello, Django!")

def manage_pricing_config(request):
    """
    View function to handle pricing configuration form submissions.
    """
    if request.method == 'POST':
        form = PricingConfigForm(request.POST)
        if form.is_valid():
            logger.info(f'User {request.user.username} created a new pricing configuration at {timezone.now()}')
            form.save()
        else:
            return render(request, 'manage_pricing_config.html', {'form': form, 'error': form.errors})
    else:
        form = PricingConfigForm()

    return render(request, 'manage_pricing_config.html', {'form': form})

class PricingCalculatorView(APIView):
    def post(self, request, format=None):
        """
        API view to calculate pricing based on provided data.
        """
        serializer = PricingCalculatorSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            tier = data['tier']
            day = data['day']
            Tn = data['Tn']
            Dn = data['Dn']

            # Retrieve the appropriate PricingConfig instance based on tier and day
            pricing_config = PricingConfig.objects.filter(tier=tier, day=day, is_active=True).first()

            if pricing_config:
                DBP = pricing_config.DBP
                DAP = pricing_config.DAP
                TMF = pricing_config.TMF
                WC = pricing_config.WC
                max_distance = pricing_config.max_km_driven
                
                Dn = max(Dn - max_distance, 0)  # Ensure Dn is non-negative
                price = ((DBP + (Dn * DAP)) + (Tn * TMF) + WC)
                return JsonResponse({'Price': price})
            else:
                return JsonResponse({'error': 'No active pricing configuration found for the specified tier and day.'}, status=400)
        else:
            return JsonResponse(serializer.errors, status=400)
