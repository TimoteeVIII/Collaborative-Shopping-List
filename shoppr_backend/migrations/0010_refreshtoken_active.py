# Generated by Django 5.0.4 on 2024-05-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppr_backend', '0009_refreshtoken_expires_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='refreshtoken',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]