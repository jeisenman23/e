# Generated by Django 2.1.4 on 2019-06-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_model_comment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='snapshot_version',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]