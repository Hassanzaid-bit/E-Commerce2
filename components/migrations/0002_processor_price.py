# Generated by Django 3.0.11 on 2021-02-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='processor',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5000, max_digits=10),
            preserve_default=False,
        ),
    ]
