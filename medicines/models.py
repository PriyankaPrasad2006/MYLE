from django.db import models
import json


class Medicine(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the medicine")
    description = models.TextField(blank=True, null=True, help_text="Medicine description")
    batch_number = models.CharField(max_length=100, unique=True, help_text="Unique batch number")
    manufacturing_date = models.DateField(help_text="Manufacturing date")
    expiry_date = models.DateField(help_text="Expiry date")
    manufacturer = models.CharField(max_length=255, help_text="Manufacturer name")
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Maximum Retail Price")
    caution = models.TextField(blank=True, null=True, help_text="Cautionary information")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Medicine"
        verbose_name_plural = "Medicines"

    def __str__(self):
        return f"{self.name} - {self.batch_number}"

    def get_qr_data(self, domain="http://127.0.0.1:8000"):
        """Returns URL for QR code that leads to medicine details page."""
        # This will generate a URL like: http://127.0.0.1:8000/medicine/DOBS3797/
        # For production, you can pass your actual domain like: https://yourdomain.com
        return f"{domain}/medicine/{self.batch_number}/"
