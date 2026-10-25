                                               

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0005_alter_community_options_alter_membership_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'ordering': ['-created_at'], 'verbose_name': 'Community', 'verbose_name_plural': 'Communities'},
        ),
    ]
