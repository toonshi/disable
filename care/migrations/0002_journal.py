# Generated by Django 5.1.2 on 2024-10-17 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
