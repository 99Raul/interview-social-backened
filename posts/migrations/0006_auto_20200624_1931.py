# Generated by Django 3.0.7 on 2020-06-24 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_relationship'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_auto_20200624_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=uuid.UUID('9237b735-9016-4328-93fb-a64b905167d1'), on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=uuid.UUID('11d157ff-7e55-438d-b061-dbec6db87dac'), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
