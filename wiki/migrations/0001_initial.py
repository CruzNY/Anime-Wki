# Generated by Django 2.0.7 on 2018-07-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('aliases', models.TextField()),
                ('age', models.SmallIntegerField()),
                ('height', models.CharField(max_length=6)),
                ('origin', models.CharField(max_length=40)),
                ('affiliations', models.TextField()),
                ('relationships', models.TextField()),
            ],
        ),
    ]
