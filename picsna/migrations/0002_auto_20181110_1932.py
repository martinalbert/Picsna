# Generated by Django 2.1.3 on 2018-11-10 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picsna', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completev',
            name='contains',
        ),
        migrations.AddField(
            model_name='detailv',
            name='completev',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='picsna.CompleteV'),
        ),
    ]
