                                               

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_alter_community_name_alter_community_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
