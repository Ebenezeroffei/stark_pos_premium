# Generated by Django 3.0.8 on 2020-10-19 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_product_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockoverview',
            old_name='stock_left',
            new_name='stock',
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('glass', 'glass'), ('bottle', 'bottle'), ('gallon', 'gallon'), ('box', 'box'), ('tin', 'tin'), ('carton', 'carton'), ('sack', 'sack'), ('bowl', 'bowl'), ('pound', 'pound'), ('kilo', 'kilo'), ('bar', 'bar'), ('packet', 'packet')], default='box', max_length=100),
        ),
        migrations.CreateModel(
            name='CostRevenueAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('total_revenue', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
