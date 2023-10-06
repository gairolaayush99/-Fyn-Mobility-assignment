from django.db import models

class PricingConfig(models.Model):
    TIER_CHOICES = (
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
        ('Luxury', 'Luxury'),
    )

    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    tier = models.CharField(max_length=20, choices=TIER_CHOICES)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    max_km_driven = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Maximum kilometers driven
    TMF = models.DecimalField(max_digits=10, decimal_places=2)  # Price per minute
    DAP = models.DecimalField(max_digits=10, decimal_places=2)  # Price per kilometer
    WC = models.DecimalField(max_digits=10, decimal_places=2)  # Waiting time fee
    is_active = models.BooleanField(default=False)  # Indicates whether this configuration is active or not
    DBP = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def save(self, *args, **kwargs):
        # If this configuration is being set as active, deactivate all other configurations
        if self.is_active:
            PricingConfig.objects.filter(is_active=True, tier=self.tier, day=self.day).update(is_active=False)
        super(PricingConfig, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.tier} Pricing - {self.day}'
