# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, verbose_name='email address', max_length=75, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('validated_at', models.DateTimeField(editable=False, null=True, default=None, verbose_name='DateTime an account is validated')),
                ('is_active', models.BooleanField(help_text='Designates whether the active flag of the user. ', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', related_query_name='user', related_name='user_set', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', to='auth.Permission', related_query_name='user', related_name='user_set', verbose_name='user permissions')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(editable=False, default=True, verbose_name='Is the object active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time object')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last time the object was updated')),
                ('title', models.CharField(verbose_name='Title', null=True, default=None, max_length=1024)),
                ('description', models.CharField(verbose_name='Description', null=True, default=None, max_length=20480)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created_by', models.ForeignKey(related_name='category_created', to=settings.AUTH_USER_MODEL, editable=False, verbose_name='User who created the object')),
                ('parent', mptt.fields.TreeForeignKey(to='unavis.Category', null=True, blank=True, related_name='children')),
                ('updated_by', models.ForeignKey(related_name='category_updated', to=settings.AUTH_USER_MODEL, editable=False, verbose_name='Last user who updated object')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(editable=False, default=True, verbose_name='Is the object active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time object')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last time the object was updated')),
                ('title', models.CharField(verbose_name='Title', null=True, default=None, max_length=1024)),
                ('description', models.CharField(verbose_name='Description', null=True, default=None, max_length=20480)),
                ('slug', models.SlugField(editable=False, verbose_name='Slug')),
                ('category', models.ForeignKey(to='unavis.Category', editable=False, related_name='pages')),
                ('created_by', models.ForeignKey(related_name='page_created', to=settings.AUTH_USER_MODEL, editable=False, verbose_name='User who created the object')),
                ('updated_by', models.ForeignKey(related_name='page_updated', to=settings.AUTH_USER_MODEL, editable=False, verbose_name='Last user who updated object')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(editable=False, default=True, verbose_name='Is the object active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time object')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last time the object was updated')),
                ('title', models.CharField(verbose_name='Title', null=True, default=None, max_length=1024)),
                ('description', models.CharField(verbose_name='Description', null=True, default=None, max_length=20480)),
                ('note', models.PositiveSmallIntegerField(default=0, verbose_name='Global note')),
                ('created_by', models.ForeignKey(related_name='review_created', to=settings.AUTH_USER_MODEL, editable=False, verbose_name='User who created the object')),
                ('page', models.ForeignKey(to='unavis.Page')),
                ('updated_by', models.ForeignKey(related_name='review_updated', to=settings.AUTH_USER_MODEL, editable=False, verbose_name='Last user who updated object')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
