# Generated by Django 4.1.5 on 2023-01-29 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=250, unique_for_date='publish'),
        ),
    ]
