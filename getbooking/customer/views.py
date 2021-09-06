from django.shortcuts import render

from getbooking.customer import forms


def appointment(request):
    booking_form = forms.CreateBookingForm()

    return render(request, 'customer/appointment.html', {
        "booking_form": booking_form
    })


def verify_mobile(request):
    return render(request, 'customer/verify.html')
