# Generated by Django 5.1.3 on 2024-11-29 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_petfood_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petfood',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
