# Generated by Django 2.2.2 on 2020-07-07 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TC_name', models.CharField(max_length=500, verbose_name='用例概述')),
                ('TC_set_up', models.TextField(verbose_name='用例前置')),
                ('TC_params', models.TextField(verbose_name='接口参数')),
                ('TC_checks', models.TextField(verbose_name='检验')),
                ('TC_next_step', models.CharField(blank=True, default='无', max_length=200, null=True, verbose_name='下一步参数')),
                ('TC_version', models.CharField(blank=True, max_length=100, null=True, verbose_name='用例版本')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用例概述',
                'verbose_name_plural': '用例概述',
            },
        ),
    ]
