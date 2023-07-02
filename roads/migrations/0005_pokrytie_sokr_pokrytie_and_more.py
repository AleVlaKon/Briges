# Generated by Django 4.1.1 on 2023-06-23 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0004_rename_pokrytia_pokrytie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokrytie',
            name='sokr_pokrytie',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Покрытие'),
        ),
        migrations.AlterField(
            model_name='pokrytieuchastka',
            name='uchastok',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pokr_uch', to='roads.uchastok', verbose_name='Участок'),
        ),
    ]