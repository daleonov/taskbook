# Generated by Django 3.2.4 on 2021-06-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskbook_app', '0002_auto_20210626_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title_machine_friendly',
            field=models.CharField(default=0, max_length=256),
            preserve_default=False,
        ),
    ]
