# Generated by Django 3.0.11 on 2021-02-03 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0002_auto_20210203_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='available',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='created',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='model',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='screen_size',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='updated',
        ),
        migrations.AddField(
            model_name='desktop',
            name='Brand',
            field=models.CharField(choices=[('Acer', 'Acer'), ('ASUS', 'ASUS'), ('HP', 'HP'), ('DELL', 'DELL'), ('MICROSOFT', 'MICROSOFT'), ('LENOVO', 'LENOVO')], default='ASUS', max_length=200),
        ),
        migrations.AddField(
            model_name='desktop',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='desktop',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desktop',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='desktop',
            name='memory',
            field=models.CharField(choices=[('4GB', '4GB'), ('8GB', '8GB'), ('16GB', '16GB')], default='8GB', max_length=200),
        ),
        migrations.AddField(
            model_name='desktop',
            name='model',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='desktop',
            name='price',
            field=models.DecimalField(decimal_places=2, default=12000, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desktop',
            name='screen_size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desktop',
            name='slug',
            field=models.SlugField(default='slug', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desktop',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='portable',
            name='Brand',
            field=models.CharField(choices=[('Acer', 'Acer'), ('ASUS', 'ASUS'), ('HP', 'HP'), ('DELL', 'DELL'), ('MICROSOFT', 'MICROSOFT'), ('LENOVO', 'LENOVO')], default='HP', max_length=200),
        ),
        migrations.AddField(
            model_name='portable',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='portable',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portable',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='portable',
            name='memory',
            field=models.CharField(choices=[('4GB', '4GB'), ('8GB', '8GB'), ('16GB', '16GB')], default='8GB', max_length=200),
        ),
        migrations.AddField(
            model_name='portable',
            name='model',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='portable',
            name='price',
            field=models.DecimalField(decimal_places=2, default=12000, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portable',
            name='screen_size',
            field=models.IntegerField(default=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portable',
            name='slug',
            field=models.SlugField(default='slug', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portable',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
