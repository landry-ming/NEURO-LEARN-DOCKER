# Generated by Django 2.1.7 on 2019-10-03 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20191003_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasets',
            name='user_id',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
