# Generated by Django 3.0.5 on 2020-04-12 21:19

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('proof_of_work', models.TextField()),
                ('previous', models.TextField()),
                ('hash', models.TextField()),
            ],
        ),
    ]
