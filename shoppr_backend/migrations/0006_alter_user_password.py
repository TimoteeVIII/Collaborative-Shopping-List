# Generated by Django 5.0.4 on 2024-05-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppr_backend', '0005_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
