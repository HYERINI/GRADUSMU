# Generated by Django 4.1 on 2022-08-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='second_universe',
            field=models.CharField(default='', max_length=50),
        ),
    ]