from django import forms
from .models import PricingConfig

class PricingConfigForm(forms.ModelForm):
    class Meta:
        model = PricingConfig
        fields = ('tier', 'day','max_km_driven','DBP',
                'TMF', 'DAP', 'WC',"is_active")

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
