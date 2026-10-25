                                               

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['is_done', '-priority']},
        ),
    ]
