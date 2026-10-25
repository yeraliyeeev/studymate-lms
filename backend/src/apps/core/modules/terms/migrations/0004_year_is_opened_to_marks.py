                                               

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terms', '0003_alter_term_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='year',
            name='is_opened_to_marks',
            field=models.BooleanField(default=False),
        ),
    ]
