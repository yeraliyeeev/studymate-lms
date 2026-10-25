                                               

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schools", "0002_school_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="school",
            name="feed",
        ),
        migrations.AlterField(
            model_name="school",
            name="name",
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
