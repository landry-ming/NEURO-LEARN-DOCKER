# Generated by Django 2.2.2 on 2019-08-24 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_demo',
            name='project_id',
            field=models.CharField(default='PROJ20190626040404', max_length=64),
            preserve_default=False,
        ),
    ]
