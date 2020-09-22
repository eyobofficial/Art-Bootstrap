# Generated by Django 3.0.7 on 2020-09-22 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0012_auto_20200922_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='bootstrap_version',
            field=models.IntegerField(choices=[(3, '3.x'), (4, '4.x'), (5, '5.x')], default=4, max_length=10),
        ),
    ]
