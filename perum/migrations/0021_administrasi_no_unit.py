# Generated by Django 3.0.6 on 2020-06-02 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perum', '0020_auto_20200602_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrasi',
            name='no_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='perum.Unit'),
        ),
    ]