# Generated by Django 3.0.6 on 2020-06-16 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perum', '0032_remove_pelanggan_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelanggan',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
