# Generated by Django 5.1.2 on 2024-11-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_alter_userselection_card_tour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userselection',
            name='number_of_people',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userselection',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая стоимость'),
        ),
    ]
