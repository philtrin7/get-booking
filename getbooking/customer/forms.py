from django import forms

from getbooking.customer.models import Customer


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('address', 'phone_number', 'date_of_birth')
