# Generated by Django 4.2.7 on 2023-11-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
