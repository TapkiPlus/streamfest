# Generated by Django 2.2.6 on 2019-12-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0010_speaker_uniqurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='uniqUrl',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Хеш для ссылки'),
        ),
    ]
