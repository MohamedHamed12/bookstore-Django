from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from .models import Customer, order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Orderform(ModelForm):
    class Meta():
        model = order
        fields = '__all__'

class Customerform(ModelForm):  
    class Meta():
        model=Customer
        fields='__all__'
        exclude = ['user'  ]
class CreateNewUser(UserCreationForm):
    class Meta():
        model=User
        fields = ['username', 'email','password1']