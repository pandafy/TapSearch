# Generated by Django 2.2.7 on 2019-11-25 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191125_0230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='words',
            old_name='Word',
            new_name='word',
        ),
    ]
