# Generated by Django 3.0.7 on 2020-09-22 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0002_delete_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ('title',), 'verbose_name': 'Technology', 'verbose_name_plural': 'Technologies'},
        ),
    ]