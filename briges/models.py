from django.db import models
from roads.models import Road

# Create your models here.

class Briges(models.Model):
    prepyat = models.CharField(max_length=255, verbose_name = 'Препятствие', null=True, default=None, blank=True)
    km = models.CharField(max_length=255, verbose_name = 'Км', null=True, default=None, blank=True)
    god_postr = models.IntegerField(verbose_name = 'Год постройки', null=True, default=None, blank=True)
    proekt_nagr = models.CharField(max_length=255, verbose_name = 'Проектные нагрузки', null=True, default=None, blank=True)
    pol_shir = models.FloatField(verbose_name = 'Полная ширина', null=True, default=None, blank=True)
    gabarit = models.FloatField(verbose_name = 'Габарит', null=True, default=None, blank=True)
    trotuar = models.FloatField(verbose_name = 'Ширина тротуара', null=True, default=None, blank=True)
    tol_dor_od = models.FloatField(verbose_name = 'Толщина дорожной одежды', null=True, default=None, blank=True)
    stat_sist = models.CharField(max_length=255, verbose_name = 'Статическая система', null=True, default=None, blank=True)
    material = models.CharField(max_length=255, verbose_name = 'Статическая система', null=True, default=None, blank=True)
    tip_proekt = models.CharField(max_length=255, null=True, verbose_name = 'Типовой проект (необязательно)', default=None, blank=True)
    prod_schema = models.CharField(max_length=255, verbose_name = 'Продольная схема', null=True, default=None, blank=True)
    poln_dlina = models.FloatField(verbose_name = 'Полная длина', null=True, default=None, blank=True)
    chis_bal = models.CharField(max_length=255, verbose_name = 'Число балок', null=True, default=None, blank=True)
    poper_schema = models.CharField(max_length=255, verbose_name = 'Поперечная схема', null=True, default=None, blank=True)
    param_bal = models.CharField(max_length=255, verbose_name = 'Параметры балки', null=True, default=None, blank=True)
    doroga = models.ForeignKey(Road, on_delete=models.PROTECT, verbose_name = 'Автодорога', null=True, default=None, blank=True)

    def __str__(self):
        return f'{self.pk} {self.prepyat} на км {self.km}'


    class Meta:
        verbose_name = 'Мосты'
        verbose_name_plural = 'Мосты'


class Dorogi(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дороги'
        verbose_name_plural = 'Дороги'
