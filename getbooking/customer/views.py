from django.shortcuts import render

from getbooking.customer import forms


def appointment(request):
    booking_form = forms.CreateBookingForm()

    return render(request, 'customer/appointment.html')
