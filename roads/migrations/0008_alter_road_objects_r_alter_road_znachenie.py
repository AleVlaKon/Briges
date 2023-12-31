# Generated by Django 4.2.2 on 2023-06-24 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0007_alter_road_objects_r_alter_road_znachenie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='road',
            name='objects_r',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='objects_names', to='roads.nameobject', verbose_name='Объекты'),
        ),
        migrations.AlterField(
            model_name='road',
            name='znachenie',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='roads.znachenie', verbose_name='Значение'),
        ),
    ]
