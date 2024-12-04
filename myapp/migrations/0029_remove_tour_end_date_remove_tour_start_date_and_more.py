# Generated by Django 5.1.2 on 2024-11-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_remove_userselection_tour_userselection_card_tour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='start_date',
        ),
        migrations.AddField(
            model_name='cardtour',
            name='end_date',
            field=models.DateField(default='2024-02-01'),
        ),
        migrations.AddField(
            model_name='cardtour',
            name='start_date',
            field=models.DateField(default='2024-01-01'),
        ),
    ]