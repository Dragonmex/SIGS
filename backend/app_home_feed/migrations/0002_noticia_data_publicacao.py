# Generated by Django 5.1.2 on 2024-11-02 04:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home_feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='data_publicacao',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
