# Generated by Django 3.1.1 on 2021-03-31 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0007_auto_20210203_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='portable',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]