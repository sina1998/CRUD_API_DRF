# Generated by Django 5.0.3 on 2024-03-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
