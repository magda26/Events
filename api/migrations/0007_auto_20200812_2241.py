# Generated by Django 3.1 on 2020-08-12 22:41

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200810_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(default='default-thumbnail.jpg', upload_to=api.models.get_path_class),
        ),
    ]
