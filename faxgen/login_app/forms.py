from django import forms
from django.contrib.auth.models import User
from login_app.models import UserInfo
# from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','email','password']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'class':'form-control'}),

        }
    # def clean(self):
    #     cleaned_data=super().clean()
    #     cpass=cleaned_data.get('password')
    #     ccpass=cleaned_data.get('password2')

    #     if cpass and ccpass:
    #         if cpass!= ccpass:
    #             raise ValidationError('Passwords not identical!')


class UserInfoForm(forms.ModelForm):
    class Meta():
        model=UserInfo
        fields=['aircraft']
        widgets={
            'aircraft':forms.Select(attrs={'class':'form-select'})
        }

