# Generated by Django 4.0.6 on 2022-07-22 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='titel',
            field=models.CharField(max_length=200),
        ),
    ]