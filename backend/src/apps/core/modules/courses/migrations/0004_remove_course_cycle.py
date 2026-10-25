                                               

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='cycle',
        ),
    ]
