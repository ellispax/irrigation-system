# Generated by Django 4.1.5 on 2023-02-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
