                                               

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('final_marks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='termmark',
            name='course',
        ),
    ]
