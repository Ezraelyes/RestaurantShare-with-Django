# Generated by Django 4.2.3 on 2023-07-30 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareRes', '0002_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='cateogory',
            new_name='category',
        ),
    ]