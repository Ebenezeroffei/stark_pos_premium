# Generated by Django 3.0.8 on 2020-11-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20201102_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetails',
            name='image',
            field=models.ImageField(default='default_company_logo.svg', upload_to='company_logo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_product_logo.svg', upload_to='product_images'),
        ),
    ]
