# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_agenda', '0002_auto_20160224_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name_plural': 'Event categories',
                'verbose_name': 'Event category',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='external_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='external_id'),
        ),
        migrations.AddField(
            model_name='event',
            name='featured',
            field=models.BooleanField(default=False, verbose_name='featured'),
        ),
        migrations.AddField(
            model_name='event',
            name='featured_image_description',
            field=models.TextField(blank=True, verbose_name='featured image description'),
        ),
        migrations.AddField(
            model_name='event',
            name='featured_image_header',
            field=mezzanine.core.fields.FileField(blank=True, max_length=1024, verbose_name='featured image header'),
        ),
        migrations.AddField(
            model_name='event',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='mezzanine_agenda.Event', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='event',
            name='allow_comments',
            field=models.BooleanField(default=False, verbose_name='Allow comments'),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='mezzanine_agenda.EventCategory', verbose_name='category'),
        ),
    ]