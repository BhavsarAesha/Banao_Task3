# Generated by Django 4.2.4 on 2024-07-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blogpost_draft_blogpost_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='status',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]