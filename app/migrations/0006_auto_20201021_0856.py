# Generated by Django 3.0.8 on 2020-10-21 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201019_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdata',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
