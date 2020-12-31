# Generated by Django 3.1 on 2020-10-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20201025_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ldapserver',
            name='ldap_server',
            field=models.CharField(choices=[('openladp', 'openladp'), ('windows_ad', 'windows_ad')], default='openldap', max_length=30, verbose_name='ldap类型'),
        ),
        migrations.AlterField(
            model_name='ldapserver',
            name='port',
            field=models.IntegerField(default=389, verbose_name='端口'),
        ),
    ]