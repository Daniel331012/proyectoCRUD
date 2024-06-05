from django import forms
from .models import tabla9, tabla10

#DECLARACION DE FORMULARIOS 
class tabla9Form(forms.ModelForm):
    class Meta:
        model = tabla9
        fields = '__all__'

class tabla10Form(forms.ModelForm):
    class Meta:
        model = tabla10
        fields = '__all__'        