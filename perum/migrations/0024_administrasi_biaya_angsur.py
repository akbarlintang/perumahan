# Generated by Django 3.0.6 on 2020-06-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perum', '0023_auto_20200608_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrasi',
            name='biaya_angsur',
            field=models.IntegerField(null=True),
        ),
    ]
