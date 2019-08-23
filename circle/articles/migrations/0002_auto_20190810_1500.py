# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-10 07:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='关联文章'),
        ),
        migrations.AddField(
            model_name='comments',
            name='parentCom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Comments', verbose_name='评论自关联父级'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='关联用户'),
        ),
        migrations.AddField(
            model_name='articletype',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleType', verbose_name='父级类型'),
        ),
        migrations.AddField(
            model_name='articlegroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='文集创建者'),
        ),
        migrations.AddField(
            model_name='article_zan_log',
            name='link_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='关联文章'),
        ),
        migrations.AddField(
            model_name='article_zan_log',
            name='link_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='关联用户'),
        ),
        migrations.AddField(
            model_name='article_count',
            name='link_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='关联文章'),
        ),
        migrations.AddField(
            model_name='article_count',
            name='link_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='关联用户'),
        ),
        migrations.AddField(
            model_name='article',
            name='articleGroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleGroup', verbose_name='关联文集'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleType', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='关联用户'),
        ),
    ]