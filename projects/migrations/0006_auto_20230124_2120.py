# Generated by Django 4.1.5 on 2023-01-24 20:20

from django.db import migrations
from django.db.models import DateTimeField
import datetime

def set_default_value(apps, schema_editor):
    Review = apps.get_model('projects', 'Review')
    for review in Review.objects.all():
        review.created = datetime.datetime.now()
        review.save()

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_options_review_owner_and_more'),
    ]

    operations = [
        migrations.RunPython(set_default_value),
        migrations.AddField(
            model_name='Review',
            name='created',
            field=DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
    ]
