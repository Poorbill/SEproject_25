# Generated by Django 2.2.6 on 2019-11-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='minsheng',
            name='phone_num',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
