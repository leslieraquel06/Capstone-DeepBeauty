# Generated by Django 5.0.3 on 2024-04-21 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skincare', '0006_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='names',
        ),
    ]
