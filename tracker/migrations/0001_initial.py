# Generated by Django 4.1 on 2022-08-12 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('ping', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('key_on_datetime', models.DateTimeField()),
                ('key_off_datetime', models.DateTimeField()),
                ('speed', models.IntegerField()),
                ('distance', models.FloatField()),
                ('cum_distance', models.IntegerField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
    ]
