# Generated by Django 4.2.3 on 2023-07-30 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shareRes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100)),
                ('restaurant_link', models.CharField(max_length=500)),
                ('restaurant_content', models.TextField()),
                ('restaurant_keyword', models.CharField(max_length=50)),
                ('cateogory', models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to='shareRes.category')),
            ],
        ),
    ]
