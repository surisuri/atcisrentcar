# Generated by Django 2.1.4 on 2018-12-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0003_auto_20181213_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='author',
        ),
        migrations.AddField(
            model_name='state',
            name='username',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]