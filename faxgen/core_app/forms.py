from django import forms
from .models import Fax_elts
from django.core.validators import FileExtensionValidator


class OperationalFPLForm(forms.Form):
        ofp=forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}),validators=[FileExtensionValidator(['pdf'])])

class Fax_eltsForm(forms.ModelForm):
    class Meta():
        model = Fax_elts
        exclude=['generated','generated_file']
        widgets = {
            'captain':forms.TextInput(attrs={'class':'form-control', 'placeholder':'x'}),
            'aircraft':forms.Select(attrs={'class':'form-select'}),
            'fir_countries':forms.Textarea(attrs={'class':'form-control',"placeholder":'Separated by comma ","' ,"style":"height: 100px;"}),
            'fir_points':forms.Textarea(attrs={'class':'form-control',"placeholder":'Separated by comma ","' , "style":"height: 100px;"}),
        }