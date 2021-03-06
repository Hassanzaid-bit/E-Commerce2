# Generated by Django 3.0.11 on 2021-02-03 07:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desktop',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='desktop',
            name='name',
        ),
        migrations.RemoveField(
            model_name='portable',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='portable',
            name='name',
        ),
        migrations.AddField(
            model_name='computer',
            name='Brand',
            field=models.CharField(choices=[('Acer', 'Acer'), ('ASUS', 'ASUS'), ('HP', 'HP'), ('DELL', 'DELL'), ('MICROSOFT', 'MICROSOFT'), ('LENOVO', 'LENOVO')], default='HP', max_length=200),
        ),
        migrations.AddField(
            model_name='computer',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='memory',
            field=models.CharField(choices=[('4GB', '4GB'), ('8GB', '8GB'), ('16GB', '16GB')], default='8GB', max_length=200),
        ),
        migrations.AddField(
            model_name='computer',
            name='model',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='computer',
            name='name',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='price',
            field=models.DecimalField(decimal_places=2, default=12000, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='screen_size',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='computer',
            name='slug',
            field=models.SlugField(default='slug', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='type',
            field=models.CharField(choices=[('Desktop', 'Desktop'), ('All-in-one', 'All-in-one')], default='Desktop', max_length=200),
        ),
        migrations.AlterField(
            model_name='portable',
            name='type',
            field=models.CharField(choices=[('', 'Laptop/Notenook'), ('2 in 1', '2 in 1'), ('Chromebook', 'Chromebook'), ('Microsoft Surface', 'Microsoft Surface')], default='Laptop/Notenook', max_length=200),
        ),
    ]
