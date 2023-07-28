from django.contrib import admin

# Register your models here.

from .models import *
from briges.models import Briges




class PokrytieUchastkaInline(admin.TabularInline):
    model = PokrytieUchastka

class BrigesInline(admin.StackedInline):
    model = Briges


class RoadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Road._meta.fields]
    list_filter = ['owner', 'znachenie']
    inlines = [PokrytieUchastkaInline]
    save_on_top = True


    class Meta:
        model = Road



class ObjectEtapInline(admin.TabularInline):
    model = ObjectEtap


class NameObjectAdmin(admin.ModelAdmin):

    inlines = [ObjectEtapInline,]



admin.site.register(Road, RoadAdmin)
admin.site.register(Pokrytie)
admin.site.register(PokrytieUchastka)
admin.site.register(Znachenie)
admin.site.register(NameObject, NameObjectAdmin)
admin.site.register(ObjectEtap)