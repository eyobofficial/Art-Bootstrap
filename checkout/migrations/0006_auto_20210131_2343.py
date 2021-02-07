# Generated by Django 3.0.7 on 2021-01-31 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20210131_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]