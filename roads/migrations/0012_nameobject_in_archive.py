# Generated by Django 4.2.2 on 2023-06-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0011_alter_road_znachenie'),
    ]

    operations = [
        migrations.AddField(
            model_name='nameobject',
            name='in_archive',
            field=models.BooleanField(default=False, verbose_name='В архиве'),
        ),
    ]
