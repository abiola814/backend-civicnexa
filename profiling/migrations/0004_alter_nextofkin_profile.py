# Generated by Django 4.2.7 on 2023-12-03 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0003_alter_userprofile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextofkin',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nextofkin', to='profiling.userprofile'),
        ),
    ]
