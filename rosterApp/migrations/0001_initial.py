# Generated by Django 4.2.2 on 2023-06-21 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('head_chef', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TradingHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_hour', models.TimeField()),
                ('closing_hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Steward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('kitchens', models.ManyToManyField(through='rosterApp.Assignment', to='rosterApp.kitchen')),
            ],
        ),
        migrations.AddField(
            model_name='kitchen',
            name='trading_hours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rosterApp.tradinghour'),
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.TextField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('steward', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rosterApp.steward')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='kitchen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rosterApp.kitchen'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='steward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rosterApp.steward'),
        ),
    ]
