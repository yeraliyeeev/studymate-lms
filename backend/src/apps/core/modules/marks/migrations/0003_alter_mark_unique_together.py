                                               

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_user'),
        ('assignments', '0001_initial'),
        ('marks', '0002_alter_mark_assignment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mark',
            unique_together={('student', 'assignment')},
        ),
    ]
