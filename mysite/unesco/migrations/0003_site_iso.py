# Generated by Django 3.2.5 on 2021-07-16 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0002_auto_20210716_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='iso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unesco.iso'),
        ),
    ]
