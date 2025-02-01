# views.py

import requests
from django.shortcuts import render,redirect

def home(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        country_code = request.POST.get('countryCode')
        full_phone = request.POST.get('fullPhone')

        # Prepare the data to send to the API
       # views.py

        api_url = 'https://api.vamsmechatronica.in/api/v1/account/register/get_otp/'
 # Replace with your actual API endpoint
        payload = {
            'mobile': phone,
            'country_code': country_code
        }

        try:
            # Send the POST request to the API
            response = requests.post(api_url, json=payload)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                 request.session['phone'] = phone
                 request.session['country_code'] = country_code

                # Extract the OTP from the response
                # Render the verification page to accept OTP
                 return redirect('verify_otp')

                # Add the OTP to the context
                
            else:
                # Handle non-200 status codes
                error_message = f"API Error: {response.status_code} {response.reason}"
                return render(request, 'home.html', {'error': error_message})
        except requests.exceptions.RequestException as e:
            # Handle exceptions
            error_message = f"An error occurred: {e}"
            return render(request, 'home.html', {'error': error_message})

    return render(request, 'home.html')

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        phone = request.session.get('phone')
        country_code = request.session.get('country_code')
       

        # Prepare the payload with OTP
        api_url = 'https://api.vamsmechatronica.in/api/v1/account/register/supplier/verify-otp/'  # Replace with your actual API endpoint
        payload = {
            'mobile': phone,
            'country_code': country_code,
            'otp': otp
        }
        print(payload)

        try:
            # Send the POST request to verify the OTP
            response = requests.post(api_url, json=payload)
            print(response.status_code)

            if response.status_code == 201:
                # Parse the JSON response
                data = response.json()

                # Extract user details
                user = data.get('user', {})
                mobileno = user.get('mobileno')
                created_at = user.get('created_at')
                email = user.get('email')
                token = data.get('token')

                # Clear the session
                request.session.flush()

                # Prepare context for template
                context = {
                    'mobileno': mobileno,
                    'created_at': created_at,
                    'email': email,
                    'token': token
                }

                # Render the user details page
                return render(request, 'userDetails.html', context)
            else:
                # Handle verification failure
                error_message = "OTP verification failed. Please try again."
                return render(request, 'success.html', {'error': error_message})
        except requests.exceptions.RequestException as e:
            # Handle exceptions
            error_message = f"An error occurred: {e}"
            return render(request, 'success.html', {'error': error_message})

    else:
        # Render the verification page to accept OTP
        return render(request, 'success.html')
