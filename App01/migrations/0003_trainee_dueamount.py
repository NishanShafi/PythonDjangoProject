# Generated by Django 4.1.2 on 2022-11-01 12:57

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App01', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='DueAmount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
    ]
