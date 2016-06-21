# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikesDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], max_length=20)),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PersonNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='sex',
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='personnotes',
            name='Person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Person'),
        ),
        migrations.AddField(
            model_name='likesdislike',
            name='Person',
            field=models.ManyToManyField(to='frontend.Person'),
        ),
    ]