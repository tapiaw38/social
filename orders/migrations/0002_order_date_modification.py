# Generated by Django 3.0.3 on 2020-04-18 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_modification',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
