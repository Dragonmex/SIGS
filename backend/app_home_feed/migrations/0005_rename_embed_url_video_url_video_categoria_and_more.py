# Generated by Django 5.1.2 on 2024-11-02 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home_feed', '0004_noticia_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='embed_url',
            new_name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='app_home_feed.categoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='descricao',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]