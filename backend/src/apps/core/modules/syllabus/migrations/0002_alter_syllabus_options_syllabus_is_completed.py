                                               

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='syllabus',
            options={'verbose_name_plural': 'Syllabuses'},
        ),
        migrations.AddField(
            model_name='syllabus',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
