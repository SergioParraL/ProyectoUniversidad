from django import forms

from .models import PersonalAdm, PersonalDocente, Representantes, Estudiantes

class RegistroPA(forms.ModelForm):
    class Meta:
        model = PersonalAdm
        fields = '__all__'


class RegistroPD(forms.ModelForm):

    class Meta:
        model = PersonalDocente
        fields = '__all__'


class RegistroRep(forms.ModelForm):

    class Meta:
        model = Representantes
        fields = '__all__'
        
         

class RegistroEst(forms.ModelForm):

    class Meta:
        model = Estudiantes
        fields = '__all__'