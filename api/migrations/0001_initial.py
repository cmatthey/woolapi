# Generated by Django 3.0.8 on 2020-07-21 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32)),
                ('group', models.CharField(default='', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]