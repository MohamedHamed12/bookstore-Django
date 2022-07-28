from dataclasses import field, fields
import django
import django_filters
from .models import *
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = order
        fields = ['b','t']
        # fields  ="__all__"
        # exclude =['t']

        
