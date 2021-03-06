# Generated by Django 3.2.9 on 2021-11-23 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('height', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('evolution_type', models.CharField(max_length=20)),
                ('evolutions', models.JSONField()),
                ('stats', models.JSONField()),
            ],
        ),
    ]
