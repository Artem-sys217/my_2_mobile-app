# Generated by Django 5.1.2 on 2024-11-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_remove_tour_explore_more_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
