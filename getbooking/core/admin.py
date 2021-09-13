from django.contrib import admin

from getbooking.customer import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['phone_number', ]


admin.site.register(models.Customer)
