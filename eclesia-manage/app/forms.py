from django import forms
from .models import Membro, Funcao, PequenoGrupo

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = '__all__'


class FuncaoForm(forms.ModelForm):
    class Meta:
        model = Funcao
        fields = '__all__'

class PequenoGrupoForm(forms.ModelForm):
    class Meta:
        model = PequenoGrupo
        fields = '__all__'
