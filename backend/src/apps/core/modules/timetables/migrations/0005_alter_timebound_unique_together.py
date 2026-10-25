                                               

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0004_room_is_active'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timebound',
            unique_together={('from_time', 'to_time')},
        ),
    ]
