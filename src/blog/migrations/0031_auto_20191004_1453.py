# Generated by Django 2.2.5 on 2019-10-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20191004_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='react',
            field=models.CharField(choices=[('none', 'None'), ('like', 'Like'), ('unlike', 'Unlike')], max_length=10, verbose_name='r'),
        ),
    ]
