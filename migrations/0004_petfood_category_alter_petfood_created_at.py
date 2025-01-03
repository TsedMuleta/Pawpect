# Generated by Django 5.1.3 on 2024-11-28 13:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='petfood',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pet_foods', to='store.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='petfood',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
