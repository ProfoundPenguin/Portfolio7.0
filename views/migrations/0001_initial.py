# Generated by Django 4.2.6 on 2023-10-31 03:13

from django.db import migrations, models
import django.db.models.deletion
import views.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=60)),
                ('job', models.CharField(max_length=60)),
                ('time', models.DecimalField(decimal_places=0, max_digits=6)),
                ('responsiblity', models.CharField(max_length=70)),
                ('about', models.TextField()),
                ('tech', models.JSONField(blank=True, null=True)),
                ('main_mockup', models.ImageField(upload_to=views.models.random_filename)),
                ('main_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mockups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mockups', models.ImageField(upload_to=views.models.random_filename)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='views.work')),
            ],
        ),
    ]
