# Generated by Django 2.1.7 on 2020-06-25 14:29

from django.db import migrations, models

# 迁移文件
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
