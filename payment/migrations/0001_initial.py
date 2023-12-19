# Generated by Django 4.2.7 on 2023-12-01 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('ref', models.CharField(max_length=200)),
                ('fee_type', models.CharField(max_length=200)),
                ('state_ID', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, choices=[('completed', 'paid'), ('failed', 'failed'), ('pending', 'pending'), ('reversed', 'reversed')], default='pending', max_length=20, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiling.userprofile')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]