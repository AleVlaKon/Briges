# Generated by Django 4.1.1 on 2023-07-28 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0017_remove_uchastok_objects_r_road_objects_r'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokrytieuchastka',
            name='uchastok',
        ),
        migrations.RemoveField(
            model_name='road',
            name='objects_r',
        ),
        migrations.AddField(
            model_name='pokrytieuchastka',
            name='road',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='pokr_dor', to='roads.road', verbose_name='Дорога'),
        ),
        migrations.AddField(
            model_name='road',
            name='category',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='road',
            name='end_uchastka',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='до'),
        ),
        migrations.AddField(
            model_name='road',
            name='etap_proekta',
            field=models.ManyToManyField(default=None, null=True, related_name='etap_names', to='roads.objectetap', verbose_name='Этапы'),
        ),
        migrations.AddField(
            model_name='road',
            name='full_lenght',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Протяженность'),
        ),
        migrations.AddField(
            model_name='road',
            name='km',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Километры'),
        ),
        migrations.AddField(
            model_name='road',
            name='osevaya_nagruzka',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Осевая нагрузка'),
        ),
        migrations.AddField(
            model_name='road',
            name='start_uchastka',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='от'),
        ),
        migrations.AlterField(
            model_name='objectetap',
            name='object_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='roads.nameobject', verbose_name='Этапы'),
        ),
        migrations.DeleteModel(
            name='Uchastok',
        ),
    ]