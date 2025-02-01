import requests
from django.shortcuts import render
from .form import SupplierAccountDetails

API_URL = "api.vamsmechatronica.in/api/v1/supplier/accounts/create/"  # Replace with your actual API endpoint

def home(request):
    response_data = None  # Initialize response data

    if request.method == "POST":
        form = SupplierAccountDetails(request.POST, request.FILES)  # Handle file uploads

        if form.is_valid():
            # Extract form data
            data = {
                "bank_account_number": form.cleaned_data["bank_account_number"],
                "bank_name": form.cleaned_data["bank_name"],
                "ifsc_code": form.cleaned_data["ifsc_code"],
                "micr_code": form.cleaned_data["micr_code"] or None,
                "branch_name": form.cleaned_data["branch_name"] or None,
                "upi_id": form.cleaned_data["upi_id"] or None,
                "phone_number": form.cleaned_data["phone_number"] or None,
                "is_verified":True,
                "supplier": form.cleaned_data["supplier"],
            }
            passbook = request.FILES["passbook"]  # Get uploaded passbook image

            # Prepare multipart/form-data payload
            files = {"passbook": (passbook.name, passbook.read(), passbook.content_type)}

            # Send data & file to API
            response = requests.post(API_URL, data=data, files=files)

            # Handle API response
            if response.status_code == 200:
                response_data = response.json()  # Parse JSON response
            else:
                response_data = {"error": f"API error: {response.status_code}"}

    else:
        form = SupplierAccountDetails()

    return render(request, "SupplierAccountDetails.html", {"form": form, "response_data": response_data})
