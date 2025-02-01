#from django.contrib import admin

# Register your models here.
#from .models import SupplierAccountDetails  # Import your model

# Register your models here
#admin.site.register(SupplierAccountDetails)
from django.contrib import admin
from .models import SupplierAccountDetails

@admin.register(SupplierAccountDetails)
class SupplierAccountDetailsAdmin(admin.ModelAdmin):
    # Columns to display in the admin table view
    list_display = (
        'id', 
        'supplier', 
        'bank_account_number', 
        'bank_name', 
        'ifsc_code', 
        'branch_name', 
        'phone_number', 
        'is_verified', 
        'created_at', 
        'updated_at'
    )
    
    # Optional: Add filters for specific fields
    list_filter = ('is_verified', 'bank_name', 'created_at')

    # Optional: Add a search bar
    search_fields = ('id', 'supplier', 'bank_account_number', 'bank_name')

    # Optional: Add pagination (default is 100 per page)
    list_per_page = 20
