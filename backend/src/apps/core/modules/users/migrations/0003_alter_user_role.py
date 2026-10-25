                                               

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_phone_alter_user_telegram_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("manager", "Manager"),
                    ("teacher", "Teacher"),
                    ("student", "Student"),
                    ("unknown", "Unknown"),
                ],
                default="unknown",
                max_length=15,
            ),
        ),
    ]
