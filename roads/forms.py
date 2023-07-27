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
    '''Форма ввода дороги'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['owner'].widget.attrs['class'] = 'form-control'
        self.fields['znachenie'].widget.attrs['class'] = 'form-select'
        self.fields['objects_r'].widget.attrs['class'] = 'form-select'


    class Meta:
        model = Road
        fields = ['number', 'name','owner','znachenie','objects_r',]


class AddUchastokForm(forms.ModelForm):
    '''Форма ввода участка дороги'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['class'] = 'form-select'
        self.fields['subnumber'].widget.attrs['class'] = 'form-control'
        self.fields['km'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['osevaya_nagruzka'].widget.attrs['class'] = 'form-control'
        self.fields['start_uchastka'].widget.attrs['class'] = 'form-control'
        self.fields['end_uchastka'].widget.attrs['class'] = 'form-control'
        self.fields['full_lenght'].widget.attrs['class'] = 'form-control'
        self.fields['etap_proekta'].widget.attrs['class'] = 'form-select'
        


    class Meta:
        model = Uchastok
        fields = ['number', 
                  'subnumber',
                  'km',
                  'category',
                  'osevaya_nagruzka',
                  'start_uchastka',
                  'end_uchastka',
                  'full_lenght',
                  'etap_proekta',
                  ]


PokrFormSet = inlineformset_factory(Uchastok, PokrytieUchastka, extra=2, fields='__all__')

class BaseUchFormset(BaseInlineFormSet):

    def add_fields(self, form, index):
        super().add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = PokrFormSet(
                        instance=form.instance,
                        data=form.data if form.is_bound else None,
                        files=form.files if form.is_bound else None,
                        prefix='pokr-%s-%s' % (
                            form.prefix, PokrFormSet.get_default_prefix()),
                        extra=2
                            )





    # def is_valid(self):
    #     result = super().is_valid()

    #     if self.is_bound:
    #         for form in self.forms:
    #             if hasattr(form, 'nested'):
    #                 result = result and form.nested.is_valid()
    #     return result
    

    # def clean(self):
    #     """
    #     If a parent form has no data, but its nested forms do, we should
    #     return an error, because we can't save the parent.
    #     For example, if the Book form is empty, but there are Images.
    #     """
    #     super().clean()

    #     for form in self.forms:
    #         if not hasattr(form, "nested") or self._should_delete_form(form):
    #             continue

    #         if self._is_adding_nested_inlines_to_empty_form(form):
    #             form.add_error(
    #                 field=None,
    #                 error=_(
    #                     "You are trying to add image(s) to a book which "
    #                     "does not yet exist. Please add information "
    #                     "about the book and choose the image file(s) again."
    #                 ),
    #             )
    

    # def save(self, commit=True):
    #     """
    #     Also save the nested formsets.
    #     """
    #     result = super().save(commit=commit)

    #     for form in self.forms:
    #         if hasattr(form, "nested"):
    #             if not self._should_delete_form(form):
    #                 form.nested.save(commit=commit)
    #     return result


    # def _is_adding_nested_inlines_to_empty_form(self, form):
    #     """
    #     Are we trying to add data in nested inlines to a form that has no data?
    #     e.g. Adding Images to a new Book whose data we haven't entered?
    #     """
    #     if not hasattr(form, "nested"):
    #         # A basic form; it has no nested forms to check.
    #         return False

    #     if is_form_persisted(form):
    #         # We're editing (not adding) an existing model.
    #         return False

    #     if not is_empty_form(form):
    #         # The form has errors, or it contains valid data.
    #         return False

    #     # All the inline forms that aren't being deleted:
    #     non_deleted_forms = set(form.nested.forms).difference(
    #         set(form.nested.deleted_forms)
    #     )

    #     # At this point we know that the "form" is empty.
    #     # In all the inline forms that aren't being deleted, are there any that
    #     # contain data? Return True if so.
    #     return any(not is_empty_form(nested_form) for nested_form in non_deleted_forms)


RoadFormset = inlineformset_factory(Road, Uchastok, extra=2, fields='__all__')

