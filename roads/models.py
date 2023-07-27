from django.db import models


# Create your models here.


class Road(models.Model):
    number = models.CharField(max_length=255, verbose_name = 'Номер', null=True, default=None, blank=True)
    name = models.CharField(max_length=255, verbose_name = 'Наименование', null=True, default=None, blank=True)
    owner = models.CharField(max_length=255, verbose_name = 'Собственник', null=True, default=None, blank=True)
    znachenie = models.ForeignKey('Znachenie', on_delete=models.SET_NULL, verbose_name = 'Значение', null=True, blank=True)
    objects_r = models.ManyToManyField('NameObject', verbose_name = 'Объекты', related_name='objects_names', null=True, default=None)


    def __str__(self):
        return f'{self.number} {self.name}'


    class Meta:
        verbose_name = 'Дорога'
        verbose_name_plural = 'Дороги'


class Uchastok(models.Model):
    number = models.ForeignKey('Road', on_delete=models.PROTECT, verbose_name = 'Номер')
    subnumber = models.IntegerField(null=True, default=None, blank=True, verbose_name = 'Номер подучастка')
    km = models.CharField(max_length=255, verbose_name = 'Километры', null=True, default=None, blank=True)
    category = models.CharField(max_length=255, verbose_name = 'Категория', null=True, default=None, blank=True)
    osevaya_nagruzka = models.CharField(max_length=255, verbose_name = 'Осевая нагрузка', null=True, default=None, blank=True)
    start_uchastka = models.CharField(max_length=255, verbose_name = 'от', null=True, default=None, blank=True)
    end_uchastka = models.CharField(max_length=255, verbose_name = 'до', null=True, default=None, blank=True)
    full_lenght = models.FloatField(verbose_name = 'Протяженность', null=True, default=None, blank=True)
    # etap_proekta = models.CharField(max_length=255, verbose_name = 'Этап', null=True, default=None, blank=True)
    # objects_r = models.ManyToManyField('NameObject', verbose_name = 'Объекты', related_name='objects_names', null=True, default=None)
    etap_proekta = models.ManyToManyField('ObjectEtap', verbose_name = 'Этапы', related_name='etap_names', null=True, default=None)


    def __str__(self):
        if self.subnumber:
            return f'{self.number.number}.{self.subnumber} {self.number.name} {self.km}'
        else:
            return f'{self.number.number} {self.number.name} {self.km}'


    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'


class Pokrytie(models.Model):
    pokrytie = models.CharField(max_length=255, verbose_name = 'Покрытие', null=True, default=None, blank=True)
    sokr_pokrytie = models.CharField(max_length=255, verbose_name = 'Сокращенное написание', null=True, default=None, blank=True)

    
    def __str__(self):
        return self.pokrytie


    class Meta:
        verbose_name = 'Покрытие'
        verbose_name_plural = 'Покрытия'


class PokrytieUchastka(models.Model):
    uchastok = models.ForeignKey('Uchastok', on_delete=models.PROTECT, verbose_name = 'Участок', related_name='pokr_uch')
    vid_pokrytia = models.ForeignKey('Pokrytie', on_delete=models.PROTECT, verbose_name = 'Вид покрытия')
    protyazhennost = models.FloatField(verbose_name = 'Протяженность вида покрытия', null=True, default=None, blank=True)

    def __str__(self):
        return f'{self.uchastok.number}. {self.vid_pokrytia} - {self.protyazhennost} км'

    class Meta:
        verbose_name = 'Покрытие на участке'
        verbose_name_plural = 'Покрытия на участках'


class Znachenie(models.Model):
    znachenie = models.CharField(max_length=255, verbose_name='Значение', null=True, default=None, blank=True)

    def __str__(self):
        return self.znachenie

    class Meta:
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'


class NameObject(models.Model):
    object_name = models.CharField(max_length=255, verbose_name='Название объекта', null=True, default=None, blank=True)
    short_object_name = models.CharField(max_length=255, verbose_name='Краткое название', null=True, default=None, blank=True)
    dogovor_number = models.CharField(max_length=255, verbose_name='Номер договора', null=True, default=None, blank=True)
    in_archive = models.BooleanField('В архиве', default=False)


    def __str__(self):
        return self.object_name

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class ObjectEtap(models.Model):
    object_name = models.ForeignKey('NameObject', on_delete=models.PROTECT, verbose_name = 'Этапы"')
    etap_number = models.CharField(max_length=255, verbose_name='Номер этапа', null=True, default=None, blank=True)
    etap_name = models.CharField(max_length=255, verbose_name='Название этапа', null=True, default=None, blank=True)


    def __str__(self):
        # return self.etap_number
        return f'{self.object_name.object_name} - {self.etap_name}'
    
    
    class Meta:
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'