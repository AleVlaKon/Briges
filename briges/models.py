from django.db import models

# Create your models here.

class Briges(models.Model):
     prepyat = models.CharField(max_length=255, verbose_name = 'Препятствие')
     km = models.CharField(max_length=255, verbose_name = 'Км')
     god_postr = models.IntegerField(verbose_name = 'Год постройки')
     proekt_nagr = models.CharField(max_length=255, verbose_name = 'Проектные нагрузки')
     pol_shir = models.FloatField(verbose_name = 'Полная ширина')
     gabarit = models.FloatField(verbose_name = 'Габарит')
     trotuar = models.FloatField(verbose_name = 'Ширина тротуара')
     tol_dor_od = models.FloatField(verbose_name = 'Толщина дорожной одежды')
     stat_sist = models.CharField(max_length=255, verbose_name = 'Статическая система')
     material = models.CharField(max_length=255, verbose_name = 'Статическая система')
     tip_proekt = models.CharField(max_length=255, null=True, verbose_name = 'Типовой проект (необязательно)')
     prod_schema = models.CharField(max_length=255, verbose_name = 'Продольная схема')
     poln_dlina = models.FloatField(verbose_name = 'Полная длина')
     chis_bal = models.CharField(max_length=255, verbose_name = 'Число балок')
     poper_schema = models.CharField(max_length=255, verbose_name = 'Поперечная схема')
     param_bal = models.CharField(max_length=255, verbose_name = 'Параметры балки')
     doroga = models.ForeignKey('Dorogi', on_delete=models.PROTECT, verbose_name = 'Автодорога')

     class Meta:
         verbose_name = 'Мосты'
         verbose_name_plural = 'Мосты'


class Dorogi(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Дороги'
        verbose_name_plural = 'Дороги'
