# accounts/forms.py

from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    terms_and_conditions = forms.BooleanField(label='I accept the terms and conditions')

    class Meta:
        model = User
        fields = ['full_name', 'email', 'physical_address', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        






# accounts/forms.py

from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['species', 'sex', 'date_of_birth', 'breed', 'production_purpose', 'about_animal']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
