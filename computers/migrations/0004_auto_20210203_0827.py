# Generated by Django 3.0.11 on 2021-02-03 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0003_auto_20210203_0755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='name',
        ),
        migrations.AlterField(
            model_name='desktop',
            name='type',
            field=models.CharField(choices=[('Desktop', 'Desktop'), ('All-in-one', 'All-in-one')], default='Desktop type', max_length=200),
        ),
        migrations.AlterField(
            model_name='portable',
            name='type',
            field=models.CharField(choices=[('', 'Laptop/Notenook'), ('2 in 1', '2 in 1'), ('Chromebook', 'Chromebook'), ('Microsoft Surface', 'Microsoft Surface')], default='Laptop type', max_length=200),
        ),
    ]
