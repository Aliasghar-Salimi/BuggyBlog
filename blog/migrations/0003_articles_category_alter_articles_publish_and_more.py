# Generated by Django 5.0.2 on 2024-03-01 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_alter_articles_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name='دسته\u200cبندی'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 1, 10, 5, 9, 262947, tzinfo=datetime.timezone.utc), verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='category',
            name='position',
            field=models.IntegerField(verbose_name='پوزیش'),
        ),
    ]
