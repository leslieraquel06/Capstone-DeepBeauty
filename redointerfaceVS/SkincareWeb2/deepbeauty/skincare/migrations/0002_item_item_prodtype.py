# Generated by Django 5.0.3 on 2024-04-19 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skincare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_prodtype',
            field=models.CharField(default='other', max_length=200),
            preserve_default=False,
        ),
    ]
