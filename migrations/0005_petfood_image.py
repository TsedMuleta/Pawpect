# Generated by Django 5.1.3 on 2024-11-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_petfood_category_alter_petfood_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='petfood',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pet_food_images/'),
        ),
    ]
