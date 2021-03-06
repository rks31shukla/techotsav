# Generated by Django 4.0.4 on 2022-05-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=70)),
                ('Branch', models.CharField(max_length=50)),
                ('Year', models.IntegerField()),
                ('Section', models.CharField(max_length=3)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact_No', models.PositiveBigIntegerField()),
                ('Roll', models.PositiveBigIntegerField(default=1)),
                ('Contest', models.CharField(max_length=200)),
            ],
        ),
    ]
