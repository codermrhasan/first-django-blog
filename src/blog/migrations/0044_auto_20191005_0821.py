# Generated by Django 2.2.5 on 2019-10-05 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_delete_likeable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
