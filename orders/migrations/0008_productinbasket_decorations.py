# Generated by Django 3.1.5 on 2021-02-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210206_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='decorations',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
