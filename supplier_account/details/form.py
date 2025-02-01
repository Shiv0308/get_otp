from django import forms

class SupplierAccountDetails(forms.Form):
    bank_account_number = forms.CharField(
        label="Bank Account Number",
        max_length=20,
        min_length=1,
        required=True
    )
    bank_name = forms.CharField(
        label="Bank Name",
        max_length=100,
        min_length=1,
        required=True
    )
    ifsc_code = forms.CharField(
        label="IFSC Code",
        max_length=11,
        min_length=1,
        required=True
    )
    micr_code = forms.CharField(
        label="MICR Code",
        max_length=9,
        required=False
    )
    branch_name = forms.CharField(
        label="Branch Name",
        max_length=100,
        required=False
    )
    upi_id = forms.CharField(
        label="UPI ID",
        max_length=50,
        required=False
    )
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=15,
        required=False
    )
    supplier = forms.IntegerField(
        label="Supplier",
        required=True
    )
    passbook = forms.ImageField(
        label="Passbook Image",
        required=True
    )
