# Generated by Django 4.2.5 on 2023-09-05 05:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('region', models.CharField(choices=[('norte', 'Norte'), ('nordeste', 'Nordeste'), ('centro_oeste', 'Centro-Oeste'), ('sudeste', 'Sudeste'), ('sul', 'Sul')], max_length=30)),
            ],
        ),
    ]
