# Generated by Django 3.0.6 on 2020-06-01 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perum', '0015_pelanggan_no_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelanggan',
            name='id_administrasi',
        ),
    ]