# Generated by Django 5.1.4 on 2024-12-21 16:49

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Category')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Husband',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('m_count', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_model')),
            ],
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5, message='5 characters minimum'), django.core.validators.MaxLengthValidator(100, message='100 characters maximum')], verbose_name='Slug')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo')),
                ('content', models.TextField(blank=True, verbose_name='Article text')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('is_published', models.BooleanField(choices=[(False, 'Draft'), (True, 'Published')], default=0, verbose_name='Status')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='women.category', verbose_name='Categories')),
                ('husband', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='woman', to='women.husband', verbose_name='Husband')),
                ('tags', models.ManyToManyField(blank=True, related_name='tags', to='women.tagpost', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Famous women info',
                'verbose_name_plural': 'Famous women info',
                'ordering': ['-time_create'],
                'indexes': [models.Index(fields=['-time_create'], name='women_women_time_cr_9f33c2_idx')],
            },
        ),
    ]
