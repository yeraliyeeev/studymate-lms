                                               

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terms', '0002_year_remove_cycle_school_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='terms', to='terms.year'),
        ),
    ]
