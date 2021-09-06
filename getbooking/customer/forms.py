from django import forms

from getbooking.customer.models import Customer


class CreateBookingForm(forms.ModelForm):

    date_of_birth = forms.DateField(
        required=True, input_formats=['%m/%d/%Y', ])

    class Meta:
        model = Customer
        fields = ('address', 'phone_number', 'date_of_birth')
