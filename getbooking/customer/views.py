import firebase_admin
from firebase_admin import credentials
from django.shortcuts import render
from django.conf import settings

from getbooking.customer import forms

cred = credentials.Certificate(settings.FIREBASE_ADMIN_CREDENTIALS)
firebase_admin.initialize_app(cred)


def appointment(request):
    booking_form = forms.CreateBookingForm()

    return render(request, 'customer/appointment.html', {
        "booking_form": booking_form
    })


def verify_mobile(request):
    return render(request, 'customer/verify.html')
