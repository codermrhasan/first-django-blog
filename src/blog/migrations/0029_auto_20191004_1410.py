# Generated by Django 2.2.5 on 2019-10-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20191004_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='react',
            field=models.CharField(choices=[('like', 'Like'), ('unlike', 'Unlike')], max_length=10),
        ),
    ]
