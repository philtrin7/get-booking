from django.contrib import admin

from getbooking.customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['phone_number', ]


admin.site.register(Customer, CustomerAdmin)
