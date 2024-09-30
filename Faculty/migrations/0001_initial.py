# Generated by Django 5.1 on 2024-09-29 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='facultys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(max_length=255)),
                ('fname', models.CharField(max_length=255)),
                ('fh_name', models.CharField(max_length=255)),
                ('fmno', models.CharField(max_length=255)),
                ('femail', models.CharField(max_length=255)),
                ('fdepartment', models.CharField(max_length=255)),
                ('fposition', models.CharField(max_length=255)),
                ('fqualification', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_Faculty',
            },
        ),
    ]