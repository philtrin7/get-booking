import firebase_admin
from firebase_admin import credentials, auth
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from getbooking.customer.models import Customer
from getbooking.customer import forms

cred = credentials.Certificate(settings.FIREBASE_ADMIN_CREDENTIALS)
firebase_admin.initialize_app(cred)


@login_required()
def appointment(request):
    booking_form = forms.CreateBookingForm()

    return render(request, 'customer/appointment.html', {
        "booking_form": booking_form
    })


def verify_mobile(request):
    if request.method == "POST":
        if request.POST.get('action') == 'verify_mobile':
            try:
                firebase_user = auth.verify_id_token(
                    request.POST.get('id_token'))
                mobile_number = firebase_user['phone_number']

                # First time verifying mobile > create User & Customer > authenticate
                if not User.objects.filter(username=mobile_number):
                    user = User.objects.create_user(username=mobile_number)
                    user.set_unusable_password()
                    user.save()

                    Customer.objects.create(
                        user=user, mobile_number=mobile_number)

                    user_auth = authenticate(request, username=user.username)
                    if user_auth is not None:
                        login(request, user_auth)
                        return redirect(reverse('customer:appointment'))

                # Returning user > authenticate
                if User.objects.filter(username=mobile_number):
                    user_auth = authenticate(request, username=mobile_number)
                    if user_auth is not None:
                        login(request, user_auth)
                        return redirect(reverse('customer:appointment'))

            except Exception as e:
                print(e)

    return render(request, 'customer/verify.html')
