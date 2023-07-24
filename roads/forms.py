from django import forms
from django.forms import ModelForm, CheckboxInput, CheckboxSelectMultiple
from django.forms.models import inlineformset_factory, BaseInlineFormSet
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

PokrFormSet = inlineformset_factory(Uchastok, PokrytieUchastka, extra=2, fields='__all__')

class BasePokrFormset(BaseInlineFormSet):

    def add_fields(self, form, index):
        super(BasePokrFormset, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = PokrFormSet(
                        instance=form.instance,
                        data=form.data if form.is_bound else None,
                        files=form.files if form.is_bound else None,
                        prefix='pokr-%s-%s' % (
                            form.prefix, PokrFormSet.get_default_prefix()))

    def is_valid(self):
        result = super(BasePokrFormset, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested'):
                    result = result and form.nested.is_valid()
        return result
    
    def save(self, commit=True):
        """
        Also save the nested formsets.
        """
        result = super().save(commit=commit)

        for form in self.forms:
            if hasattr(form, "nested"):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result
    


    def clean(self):
        """
        If a parent form has no data, but its nested forms do, we should
        return an error, because we can't save the parent.
        For example, if the Book form is empty, but there are Images.
        """
        super().clean()

        for form in self.forms:
            if not hasattr(form, "nested") or self._should_delete_form(form):
                continue

            if self._is_adding_nested_inlines_to_empty_form(form):
                form.add_error(
                    field=None,
                    error=_(
                        "You are trying to add image(s) to a book which "
                        "does not yet exist. Please add information "
                        "about the book and choose the image file(s) again."
                    ),
                )




RoadFormset = inlineformset_factory(Road, Uchastok, extra=2, fields='__all__', formset=BasePokrFormset)








