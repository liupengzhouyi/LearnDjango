# Generated by Django 2.1.7 on 2020-06-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('paassword', models.CharField(max_length=20)),
                ('maxCardNumbers', models.IntegerField(default=3)),
                ('maxBloodValue', models.IntegerField(default=100)),
                ('bloodValue', models.IntegerField(default=99)),
                ('maxMagicValue', models.IntegerField(default=100)),
                ('magicValue', models.IntegerField(default=99)),
            ],
        ),
    ]
