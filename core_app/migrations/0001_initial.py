# Generated by Django 4.2 on 2024-07-23 04:43

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('chapter', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SystemPrompt',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('character', models.CharField(max_length=100, unique=True)),
                ('prompt', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, null=True)),
                ('system_prompt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core_app.systemprompt')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gpt_model', models.CharField(max_length=100)),
                ('chat_history', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None)),
                ('meta_data', models.JSONField(blank=True, default=dict, null=True)),
                ('knowledge', models.TextField(blank=True, default='', null=True)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.systemprompt')),
            ],
        ),
    ]
