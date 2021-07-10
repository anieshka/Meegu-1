# Generated by Django 3.2.4 on 2021-07-08 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0002_auto_20210708_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='member',
        ),
        migrations.AddField(
            model_name='project',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectmanager.member'),
        ),
    ]
