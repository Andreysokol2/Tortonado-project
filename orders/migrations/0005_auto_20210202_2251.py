# Generated by Django 3.1.5 on 2021-02-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210129_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinbasket',
            old_name='price_per_item',
            new_name='price_per_kilogram',
        ),
        migrations.RemoveField(
            model_name='productinbasket',
            name='nub',
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
