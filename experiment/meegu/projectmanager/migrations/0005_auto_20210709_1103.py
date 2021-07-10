# Generated by Django 3.2.4 on 2021-07-09 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0004_auto_20210709_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='authors', to='projectmanager.Book'),
        ),
    ]
