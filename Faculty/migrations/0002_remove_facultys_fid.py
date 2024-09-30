from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultys',
            name='fid',
        ),
    ]
