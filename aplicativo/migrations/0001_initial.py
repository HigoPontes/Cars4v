# Generated by Django 5.1.2 on 2024-11-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('filename', models.CharField(max_length=50)),
            ],
        ),
    ]
