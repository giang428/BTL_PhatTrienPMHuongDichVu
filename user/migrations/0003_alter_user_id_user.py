# Generated by Django 4.0.6 on 2023-04-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_is_vip_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_user',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
