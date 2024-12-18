# Generated by Django 5.1.2 on 2024-11-17 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_cardtour_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_people', models.PositiveIntegerField(default=1)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.hotel')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tour')),
            ],
        ),
    ]
