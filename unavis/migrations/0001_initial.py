# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(unique=True, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(verbose_name='groups', related_query_name='user', to='auth.Group', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True)),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_query_name='user', to='auth.Permission', related_name='user_set', help_text='Specific permissions for this user.', blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is the object active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time object')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last time the object was updated')),
                ('title', models.CharField(null=True, max_length=1024, default=None, verbose_name='Title')),
                ('description', models.CharField(null=True, max_length=20480, default=None, verbose_name='Description')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('created_by', models.ForeignKey(editable=False, verbose_name='User who created the object', to=settings.AUTH_USER_MODEL, related_name='category_created')),
                ('parent', mptt.fields.TreeForeignKey(null=True, blank=True, to='unavis.Category', related_name='children')),
                ('updated_by', models.ForeignKey(editable=False, verbose_name='Last user who updated object', to=settings.AUTH_USER_MODEL, related_name='category_updated')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is the object active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time object')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last time the object was updated')),
                ('title', models.CharField(null=True, max_length=1024, default=None, verbose_name='Title')),
                ('description', models.CharField(null=True, max_length=20480, default=None, verbose_name='Description')),
                ('slug', models.SlugField(editable=False, verbose_name='Slug')),
                ('category', models.ForeignKey(editable=False, to='unavis.Category', related_name='pages')),
                ('created_by', models.ForeignKey(editable=False, verbose_name='User who created the object', to=settings.AUTH_USER_MODEL, related_name='page_created')),
                ('updated_by', models.ForeignKey(editable=False, verbose_name='Last user who updated object', to=settings.AUTH_USER_MODEL, related_name='page_updated')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is the object active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time object')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last time the object was updated')),
                ('title', models.CharField(null=True, max_length=1024, default=None, verbose_name='Title')),
                ('description', models.CharField(null=True, max_length=20480, default=None, verbose_name='Description')),
                ('note', models.PositiveSmallIntegerField(default=0, verbose_name='Global note')),
                ('created_by', models.ForeignKey(editable=False, verbose_name='User who created the object', to=settings.AUTH_USER_MODEL, related_name='review_created')),
                ('page', models.ForeignKey(to='unavis.Page')),
                ('updated_by', models.ForeignKey(editable=False, verbose_name='Last user who updated object', to=settings.AUTH_USER_MODEL, related_name='review_updated')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
