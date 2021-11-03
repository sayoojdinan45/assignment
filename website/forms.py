from django import forms
from django.forms import fields
from . models import ProductTable,SignUp
class SignUpForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=8)
    ConfirmPassword=forms.CharField(label='Confirm Password',widget=forms.PasswordInput,max_length=8,min_length=8)
    class Meta():
        model=SignUp
        fields='__all__'
class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=SignUp
        fields=('Email','Password',)        
class UpdateForm(forms.ModelForm):
    class Meta():
        model=SignUp
        fields=('Name','Designation','Email','Pic','Phone')
class ChangePasswordForm(forms.Form):
    Oldpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=8)
    Newpassword=forms.CharField(widget=forms.PasswordInput,max_length=8)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8)
            
class ProductForm(forms.Form):
    class Meta():
        model=ProductTable
        fields='__all__'

   