                                               

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("grades", "0003_alter_grade_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grade",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
