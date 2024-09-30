# Generated by Django 5.1 on 2024-09-30 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=255)),
                ('dept_code', models.CharField(max_length=255)),
                ('hod_name', models.CharField(max_length=255)),
                ('dept_location', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=255)),
                ('email_address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_department',
            },
        ),
    ]
