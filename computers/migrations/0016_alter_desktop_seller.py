# Generated by Django 3.2 on 2021-05-11 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('computers', '0015_auto_20210511_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='seller',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='desktops', to=settings.AUTH_USER_MODEL),
        ),
    ]
