from django.db import models
import random

class SupplierAccountDetails(models.Model):
    id = models.CharField(primary_key=True, max_length=5, unique=True, editable=False)  # Custom 5-digit ID
    supplier = models.IntegerField()  # Supplier field added
    bank_account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=11)
    micr_code = models.CharField(max_length=9, null=True, blank=True)
    branch_name = models.CharField(max_length=100, null=True, blank=True)
    upi_id = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_verified = models.BooleanField(default=True, editable=False)  # Always True, non-editable
    created_at = models.DateTimeField(auto_now_add=True)  # Created at timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Updated at timestamp
    passbook_image = models.URLField(max_length=200, null=True, blank=True)  # URL for passbook image

    def save(self, *args, **kwargs):
        if not self.id:  # Generate ID only if it doesn't exist
            self.id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        while True:
            # Generate a random 5-digit number
            unique_id = str(random.randint(10000, 99999))
            # Check if the ID already exists in the database
            if not SupplierAccountDetails.objects.filter(id=unique_id).exists():
                return unique_id
def __str__(self):
    return f"{self.bank_name} - {self.bank_account_number}"