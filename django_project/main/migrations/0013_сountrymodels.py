# Generated by Django 5.0 on 2023-12-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_cards_size_warning'),
    ]

    operations = [
        migrations.CreateModel(
            name='СountryModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название страны:')),
                ('country_code', models.CharField(max_length=5, verbose_name='Код страны')),
            ],
        ),
    ]
