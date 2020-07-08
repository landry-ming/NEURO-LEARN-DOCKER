# Generated by Django 2.2.2 on 2019-07-28 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=64)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data_Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(max_length=64, unique=True)),
                ('data_name', models.CharField(max_length=64, unique=True)),
                ('data_path', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Projects_Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=64, unique=True)),
                ('label', models.CharField(max_length=64, unique=True)),
                ('title', models.CharField(max_length=128, unique=True)),
                ('introduction', models.TextField(max_length=4096)),
                ('methods', models.TextField(max_length=4096)),
                ('flowchart_url', models.CharField(max_length=128)),
                ('workflows_url', models.CharField(max_length=128)),
                ('templates_url', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions_Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=64, unique=True)),
                ('task_name', models.CharField(max_length=64)),
                ('task_type', models.CharField(max_length=64)),
                ('project_name', models.CharField(max_length=64)),
                ('train_data', models.CharField(max_length=1024)),
                ('enable_test', models.BooleanField()),
                ('test_data', models.CharField(max_length=1024)),
                ('label', models.CharField(max_length=64)),
                ('feat_sel', models.CharField(max_length=64)),
                ('estimator', models.CharField(max_length=64)),
                ('cv_type', models.CharField(max_length=64)),
                ('note', models.CharField(max_length=64)),
                ('verbose', models.BooleanField()),
                ('task_status', models.CharField(max_length=64)),
                ('task_result', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions_SA_Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=64, unique=True)),
                ('task_name', models.CharField(max_length=64)),
                ('task_type', models.CharField(max_length=64)),
                ('project_name', models.CharField(max_length=64)),
                ('test_var_data_x', models.CharField(max_length=1024)),
                ('group_var_data_y', models.CharField(max_length=1024)),
                ('note', models.CharField(max_length=64)),
                ('verbose', models.BooleanField()),
                ('task_status', models.CharField(max_length=64)),
                ('task_result', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='User_Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=64, unique=True)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]
