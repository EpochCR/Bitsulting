# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, db_index=True)),
                ('slug', models.SlugField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=256)),
                ('slug', models.SlugField(unique=True, max_length=256)),
                ('body', models.TextField(unique=True)),
                ('posted', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('bitcoinAddress', models.CharField(max_length=35)),
                ('reward_value', models.CharField(default=b'0.00001000', max_length=17)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='bitsulting.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bitcoinAddress', models.CharField(max_length=35)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('question', models.ForeignKey(to='bitsulting.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
