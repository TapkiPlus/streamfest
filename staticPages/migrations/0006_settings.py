# Generated by Django 2.2.7 on 2019-12-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticPages', '0005_auto_20191224_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showTwitch', models.BooleanField(default=False, verbose_name='Показывать твич?')),
            ],
        ),
    ]