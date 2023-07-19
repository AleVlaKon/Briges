from django import forms
from django.forms import ModelForm, CheckboxInput, CheckboxSelectMultiple
from django.forms.models import inlineformset_factory
from django.forms import formset_factory
from .models import *


class FilterForm(forms.Form):
    prinadlezhnost = forms.ModelChoiceField(queryset=Znachenie.objects.all(), widget=CheckboxSelectMultiple)



# class AddUchastokForm(forms.ModelForm):
#     class Meta:
#         model = Uchastok
#         fields = '__all__'
#
#
# # UchastokFormSet = formset_factory(AddUchastokForm, extra=3)
#
#
class AddRoadForm(forms.ModelForm):
    class Meta:
        model = Road
        fields = '__all__'
#
RoadFormset = inlineformset_factory(Road, Uchastok, extra=2, fields='__all__')
PokrFormSet = inlineformset_factory(Uchastok, PokrytieUchastka, extra=2, fields='__all__')










