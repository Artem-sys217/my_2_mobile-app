# Generated by Django 5.1.2 on 2024-11-17 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_remove_tour_end_date_remove_tour_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userselection',
            name='card_tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cardtour'),
        ),
        migrations.AlterField(
            model_name='userselection',
            name='number_of_people',
            field=models.PositiveIntegerField(),
        ),
    ]
