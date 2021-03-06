# Generated by Django 3.0.6 on 2020-05-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('no_telp', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('no_unit', models.CharField(max_length=5, null=True)),
                ('id_administrasi', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_unit', models.CharField(max_length=5, null=True)),
                ('id_lokasi', models.IntegerField(null=True)),
                ('tipe_unit', models.CharField(max_length=10, null=True)),
                ('foto_rumah', models.CharField(max_length=64, null=True)),
                ('status_rumah', models.CharField(choices=[('Tersedia', 'Tersedia'), ('Tidak Tersedia', 'Tidak Tersedia')], max_length=200, null=True)),
            ],
        ),
    ]
