# Generated by Django 4.0.6 on 2022-08-07 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempuser',
            name='device_id',
        ),
        migrations.AlterField(
            model_name='tempuser',
            name='d_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.device'),
        ),
    ]
