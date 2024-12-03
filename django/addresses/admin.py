from django.contrib import admin

from addresses.models import Address, City

admin.site.register(Address)
admin.site.register(City)
