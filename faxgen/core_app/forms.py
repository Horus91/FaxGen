from django import forms
from .models import OperationalFPL

class OperationalFPLForm(forms.ModelForm):
    class Meta():
        model=OperationalFPL
        fields='__all__'

