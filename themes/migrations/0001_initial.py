# Generated by Django 3.0.7 on 2020-09-22 21:11

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('subtitle', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('theme_version', models.CharField(blank=True, default='', max_length=10)),
                ('bootstrap_version', models.IntegerField(choices=[(3, '3.x'), (4, '4.x'), (5, '5.x')], default=4)),
                ('is_published', models.BooleanField(default=True, verbose_name='published')),
                ('is_featured', models.BooleanField(default=False, verbose_name='featured')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('file', models.FileField(blank=True, help_text='Archived theme file.', null=True, upload_to='', verbose_name='theme file')),
                ('preview_url', models.URLField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('download_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='themes.Category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('technologies', models.ManyToManyField(blank=True, to='themes.Technology')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ThemeFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=255)),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='themes.Theme')),
            ],
            options={
                'order_with_respect_to': 'theme',
            },
        ),
    ]