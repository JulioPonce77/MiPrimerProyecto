# Generated by Django 5.1.1 on 2024-10-02 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauthentication', '0002_alter_customuserauthentication_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserauthentication',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuserauthentication',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
