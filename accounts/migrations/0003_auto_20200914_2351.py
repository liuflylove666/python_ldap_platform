# Generated by Django 3.1 on 2020-09-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200912_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='mark',
            field=models.CharField(default=1, max_length=20, unique=True, verbose_name='角色代号'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, to='accounts.Role', verbose_name='拥有的所有角色'),
        ),
    ]
