# Generated by Django 4.1.5 on 2023-02-01 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['is_read', '-created']},
        ),
    ]