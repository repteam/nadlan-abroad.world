# Generated by Django 5.0 on 2023-12-04 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_cards_desc_alter_cards_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Галерея'},
        ),
    ]
