# Generated by Django 5.0.7 on 2024-07-19 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='body',
            new_name='review_text',
        ),
        migrations.RemoveField(
            model_name='review',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
    ]
