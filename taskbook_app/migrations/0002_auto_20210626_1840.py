# Generated by Django 3.2.4 on 2021-06-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskbook_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='course',
        ),
        migrations.AddField(
            model_name='task',
            name='course',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='task',
            name='section',
        ),
        migrations.AddField(
            model_name='task',
            name='section',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]