# Generated by Django 2.2 on 2020-06-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200602_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=1651131),
            preserve_default=False,
        ),
    ]
