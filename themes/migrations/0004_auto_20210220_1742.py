# Generated by Django 3.1.6 on 2021-02-20 14:42

from django.db import migrations, models
import themes.models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0003_auto_20200923_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='file',
            field=models.FileField(blank=True, help_text='Archived theme file.', null=True, upload_to=themes.models.themes_upload_location, verbose_name='theme file'),
        ),
    ]