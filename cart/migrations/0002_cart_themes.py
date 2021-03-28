# Generated by Django 3.1.6 on 2021-03-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='themes',
            field=models.ManyToManyField(blank=True, related_name='carts', to='themes.Theme'),
        ),
    ]