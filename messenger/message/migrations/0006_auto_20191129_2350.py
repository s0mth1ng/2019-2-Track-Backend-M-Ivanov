# Generated by Django 2.2.5 on 2019-11-29 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20191126_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Image'), (2, 'Video'), (3, 'Voice message')], default=1),
        ),
        migrations.AlterField(
            model_name='message',
            name='added_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]