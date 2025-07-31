from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the medicine")
    batch_number = models.CharField(max_length=100, unique=True, help_text="Unique batch number")
    manufacturing_date = models.DateField(help_text="Manufacturing date")
    expiry_date = models.DateField(help_text="Expiry date")
    manufacturer = models.CharField(max_length=255, help_text="Manufacturer name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Medicine"
        verbose_name_plural = "Medicines"

    def __str__(self):
        return f"{self.name} - {self.batch_number}"

    def get_qr_data(self):
        """Combines medicine data into a string for QR code."""
        return f"Medicine: {self.name}\nBatch: {self.batch_number}\nMfg Date: {self.manufacturing_date}\nExp Date: {self.expiry_date}\nManufacturer: {self.manufacturer}"
