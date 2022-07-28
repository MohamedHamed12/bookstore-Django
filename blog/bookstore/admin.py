import imp
from django.contrib import admin

# from .models import Customer
from .models import *
admin.site.register(Customer)
admin.site.register(book)
admin.site.register(order)
admin.site.register(tag)
# Register your models here.
