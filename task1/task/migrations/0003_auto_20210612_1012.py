# Generated by Django 3.1.3 on 2021-06-12 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20210612_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='level',
        ),
        migrations.RemoveField(
            model_name='table',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='table',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='table',
            name='tree_id',
        ),
        migrations.AlterField(
            model_name='table',
            name='parent',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='task.table'),
        ),
    ]
