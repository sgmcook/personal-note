# Generated by Django 4.0.5 on 2022-06-29 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('body', models.TextField(max_length=2000, null=True)),
                ('archive_flag', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]
