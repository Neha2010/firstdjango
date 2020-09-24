from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.core import validators
from django import forms
from neha.models import reg

user=get_user_model()

class RegForm(forms.ModelForm):
    class Meta:
        model = reg # # this register is used to specify for which model , django has to create form
        exclude = ()  # THIS ROW
        fields = '__all__'


class RegForm(forms.ModelForm):
    class Meta:
        model = reg #this register is used to specify for which model , django has to create form
        #exclude = ()  # THIS ROW
        fields = ['email','password']


                                                                        




"""
Validations to be applied
1. cant leave any field blank in the form -- done
2. using django. auth functionality for password validation (numeric , min length, alphanumeric etc) available in settings
 -- did it with regex
 --with Django auth ????
  auth_validate_password in django - provide options - import in forms 
  and while creating forms .. specify all fields of form like
  password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
  on which the validation is to be applied
  
3. No numeric entry in name- done
4. No emoji entry in any field
5. unique email : pop up should come when entering registered email
6. Creating session -- done

"""