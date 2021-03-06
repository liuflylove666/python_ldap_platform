# Generated by Django 3.1 on 2020-10-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20201025_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ldapserver',
            name='password',
            field=models.CharField(max_length=100, verbose_name='管理密码'),
        ),
        migrations.AlterField(
            model_name='ldapserver',
            name='port',
            field=models.IntegerField(verbose_name='端口'),
        ),
        migrations.AlterField(
            model_name='ldapserver',
            name='user',
            field=models.CharField(max_length=100, verbose_name='管理用户'),
        ),
    ]
