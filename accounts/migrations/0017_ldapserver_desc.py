# Generated by Django 3.1 on 2020-10-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20201025_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='ldapserver',
            name='desc',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
