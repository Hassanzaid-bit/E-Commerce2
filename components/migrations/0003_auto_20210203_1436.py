# Generated by Django 3.0.11 on 2021-02-03 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_processor_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hard_Drive',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('category', models.CharField(choices=[('Internal', (('Desktop Hard Drives', 'Desktop Hard Drives'), ('Laptop Hard Drives', 'Laptop Hard Drives'))), ('External', (('Desktop Hard Drives', 'Desktop Hard Drives'), ('Laptop Hard Drives', 'Laptop Hard Drives'))), ('Portable External Hard Drives', 'Portable External Hard Drives'), ('Mac Hard Drives', 'Mac Hard Drives')], default='Portable EXternal Hard Drives', max_length=200)),
                ('brand', models.CharField(default='WD', max_length=200)),
                ('series', models.CharField(default='Red Pro', max_length=200)),
                ('model', models.CharField(default='WD4003FFBX', max_length=200)),
                ('capacity', models.CharField(default='4TB', max_length=200)),
                ('manufacturer', models.CharField(choices=[('Seagate', 'Seagate'), ('Toshiba', 'Toshiba'), ('Dell', 'Dell'), ('GoHardDrive', 'GoHardDrive'), ('Hitachi', 'Hitachi')], default='Seagate', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('system', models.CharField(choices=[('Desktop Memory', 'Desktop Memory'), ('Laptop Memory', 'Laptop Memory'), ('Mac Memory', 'Mac Memory')], default='Laptop', max_length=200)),
                ('type', models.CharField(choices=[('DDR4', 'DDR4'), ('DDR3', 'DDR3'), ('DDR2', 'DDR2')], default='DDR4', max_length=200)),
                ('speed', models.CharField(choices=[('DDR4 5100', 'DDR4 5100'), ('DDR4 5000', 'DDR4 5000'), ('DDR4 4800', 'DDR4 4800'), ('DDR4 4600', 'DDR4 4600'), ('DDR4 4500', 'DDR4 4500'), ('DDR4 4400', 'DDR4 4400')], default='DDR4 5100', max_length=200)),
                ('capacity', models.CharField(default='16GB', max_length=200)),
                ('brand', models.CharField(default='CORSAIR', max_length=200)),
                ('series', models.CharField(default='Vengeance RGB Pro SL', max_length=200)),
                ('model', models.CharField(default='CMH16GX4M2D3600C18', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('type', models.CharField(choices=[('Intel', 'Intel'), ('AMD', 'AMD')], default='AMD', max_length=200)),
                ('cpu_socket_type', models.CharField(blank=True, max_length=200)),
                ('cpu_type', models.CharField(blank=True, max_length=200)),
                ('brand', models.CharField(default='GIGABIT', max_length=200)),
                ('model', models.CharField(default='Z590I AORUS ULTRA', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('category', models.CharField(choices=[('Internal SSD', 'Internal SSD'), ('External SSD', 'External SSD')], default='Internal SSD', max_length=200)),
                ('brand', models.CharField(default='SAMSUNG', max_length=200)),
                ('series', models.CharField(default='860 EVO Series', max_length=200)),
                ('model', models.CharField(default='MZ-76E500B/AM', max_length=200)),
                ('capacity', models.CharField(default='500GB', max_length=200)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('components.component',),
        ),
        migrations.AlterField(
            model_name='processor',
            name='memory_types',
            field=models.CharField(choices=[('DDR4', 'DDR4'), ('DDR3', 'DDR3'), ('DDR2', 'DDR2')], max_length=200),
        ),
    ]
