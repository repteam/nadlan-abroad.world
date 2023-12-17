# Generated by Django 5.0 on 2023-12-04 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_gallery_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='desc',
            field=models.TextField(max_length=500, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.cards'),
        ),
    ]
