# Generated by Django 5.0 on 2023-12-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.TextField(default=1, verbose_name='created_at'),
            preserve_default=False,
        ),
    ]
