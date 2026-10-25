                                               

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_alter_winner_course_alter_winner_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='award',
            options={'ordering': ('-created_at',)},
        ),
    ]
