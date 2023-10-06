
# Register your models here.
from django.contrib import admin
from .models import PricingConfig
import logging
from loguru import logger

class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ('tier', 'day','max_km_driven','DBP',
                    'TMF', 'DAP', 'WC',"is_active")

    def save_model(self, request, obj, form, change):
        # If is_active is set to True, deactivate all other configurations with the same tier and day
        if change:
            logger.info(f'User {request.user.username} edited PricingConfig with ID {obj.id}')
        else:
            logger.info(f'User {request.user.username} added a new PricingConfig with ID {obj.id}')
        if obj.is_active:
            PricingConfig.objects.filter(tier=obj.tier, day=obj.day).exclude(pk=obj.pk).update(is_active=False)
            obj.save()

admin.site.register(PricingConfig, PricingConfigAdmin)
