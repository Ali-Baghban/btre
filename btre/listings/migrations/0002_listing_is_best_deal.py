# Generated by Django 2.2.5 on 2019-09-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_best_deal',
            field=models.BooleanField(default=False),
        ),
    ]
