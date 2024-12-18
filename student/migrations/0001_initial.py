# Generated by Django 5.1 on 2024-09-30 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=255)),
                ('sname', models.CharField(max_length=255)),
                ('ssubject', models.CharField(max_length=255)),
                ('ssubcode', models.CharField(max_length=255)),
                ('sdepartment', models.CharField(max_length=255)),
                ('smno', models.CharField(max_length=255)),
                ('semail', models.CharField(max_length=255)),
                ('smname', models.CharField(max_length=255)),
                ('sfname', models.CharField(max_length=255)),
                ('saddress', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_student',
            },
        ),
    ]
