from django import forms
from .models import DocsDB,NotasDB

class Docs(forms.ModelForm):
    class Meta:
        model = DocsDB
        fields = '__all__'
        
class Notas(forms.ModelForm):
    class Meta:
        model = NotasDB
        fields = '__all__'