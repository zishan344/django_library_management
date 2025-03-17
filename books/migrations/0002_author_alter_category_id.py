# Generated by Django 5.1.6 on 2025-03-16 08:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('5dfd9db0-40e7-45cd-8c5c-dfcfd8940b98'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('biography', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8f24fae9-5112-4df1-834a-a9c2565ccb1a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
