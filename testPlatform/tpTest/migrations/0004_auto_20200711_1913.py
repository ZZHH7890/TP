# Generated by Django 2.2 on 2020-07-11 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpTest', '0003_auto_20200707_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcases',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]