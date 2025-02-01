from django.shortcuts import render,HttpResponse,redirect
from register.models import SupplierAccountDetails

# Create your views here.
# def sup_response(request): 
 #   suppliers = SupplierAccountDetails.objects.all()
  #  return render(request, 'supplier_list.html', {'suppliers': suppliers})



   
def home_register(request):
    return render(request,'register.html')
def sup_register(request):
      if request.method == 'POST':
        # Retrieve form data
        supplier = request.POST.get('supplier')
        bank_account_number = request.POST.get('bank_account_number')
        bank_name = request.POST.get('bank_name')
        ifsc_code = request.POST.get('ifsc_code')
        micr_code = request.POST.get('micr_code')
        branch_name = request.POST.get('branch_name')
        upi_id = request.POST.get('upi_id')
        phone_number = request.POST.get('phone_number')
        
        # Save the new record in the database
        new_supplier = SupplierAccountDetails.objects.create(
            supplier=supplier,
            bank_account_number=bank_account_number,
            bank_name=bank_name,
            ifsc_code=ifsc_code,
            micr_code=micr_code,
            branch_name=branch_name,
            upi_id=upi_id,
            phone_number=phone_number
        )
        
        # Send the saved object to the template
        return render(request, 'supplier_list.html', {'supplier': new_supplier})

      return render(request, 'register.html')  # If it's a GET request, show the form

      
        
    
