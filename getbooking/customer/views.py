import firebase_admin
from firebase_admin import credentials, auth
from django.shortcuts import render
from django.conf import settings

from django.contrib.auth.models import User
from getbooking.customer.models import Customer
from getbooking.customer import forms

cred = credentials.Certificate(settings.FIREBASE_ADMIN_CREDENTIALS)
firebase_admin.initialize_app(cred)


def appointment(request):
    booking_form = forms.CreateBookingForm()

    return render(request, 'customer/appointment.html', {
        "booking_form": booking_form
    })


def verify_mobile(request):
    if request.method == "POST":
        if request.POST.get('action') == 'verify_phone':
            try:
                firebase_user = auth.verify_id_token(
                    request.POST.get('id_token'))
                phone_number = firebase_user['phone_number']

                if not User.objects.filter(username=phone_number):
                    user = User.objects.create_user(username=phone_number)
                    user.set_unusable_password()
                    user.save()

                    Customer.objects.create(
                        user=user, phone_number=phone_number)

            except Exception as e:
                print(e)

    return render(request, 'customer/verify.html')
