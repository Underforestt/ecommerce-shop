# Generated by Django 3.1.7 on 2021-04-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
