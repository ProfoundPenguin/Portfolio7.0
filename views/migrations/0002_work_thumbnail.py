# Generated by Django 4.2.6 on 2023-10-31 07:40

from django.db import migrations, models
import views.models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=views.models.random_filename),
        ),
    ]
