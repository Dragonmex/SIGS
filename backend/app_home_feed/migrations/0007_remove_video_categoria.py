# Generated by Django 5.1.2 on 2024-11-02 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_home_feed', '0006_remove_linkrapido_icone_remove_linkrapido_nome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='categoria',
        ),
    ]