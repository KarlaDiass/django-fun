# Generated by Django 3.1.5 on 2021-01-19 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0005_auto_20210119_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
