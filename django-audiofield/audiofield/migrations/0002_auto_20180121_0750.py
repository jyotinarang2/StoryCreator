# Generated by Django 2.0.1 on 2018-01-21 07:50

import audiofield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audiofield', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='audio_file',
            field=audiofield.fields.AudioField(blank=True, upload_to='upload/audiofiles', verbose_name='audio file'),
        ),
    ]
