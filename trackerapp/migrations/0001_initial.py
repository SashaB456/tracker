# Generated by Django 5.1.7 on 2025-03-29 17:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Done', 'Done'), ('In progress', 'In progress'), ('Delayed', 'Delayed'), ('Deleted', 'Deleted'), ('Not started', 'Not started')], default='Not started', max_length=15)),
                ('priority', models.CharField(choices=[('Urgent', 'Urgent'), ('Important', 'Important'), ('Okay', 'Okay')], default='Okay', max_length=18)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
