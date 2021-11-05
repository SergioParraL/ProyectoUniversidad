from django import forms
from Institucion.models import PA_profile, PD_profile
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


#-------- Profiles ----------

class registerProfilePA(forms.ModelForm):
    class Meta:
        model = PA_profile
        fields = '__all__'


class registerProfilePD(forms.ModelForm):

    class Meta:
        model = PD_profile
        fields = '__all__'