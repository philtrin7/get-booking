from django.contrib import admin

from getbooking.customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(Customer, CustomerAdmin)
