# Generated by Django 2.2.5 on 2019-10-02 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191002_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blog_description',
            field=models.TextField(blank=True, max_length=124, null=True),
        ),
    ]
