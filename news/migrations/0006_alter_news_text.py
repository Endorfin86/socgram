# Generated by Django 4.1.3 on 2023-01-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_likes_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]
