# Generated by Django 3.0.11 on 2021-02-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0006_auto_20210203_0909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portable',
            options={'ordering': ('Brand',)},
        ),
        migrations.AlterField(
            model_name='desktop',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='portable',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
