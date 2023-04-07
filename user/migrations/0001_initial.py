# Generated by Django 4.1.7 on 2023-04-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id_user", models.IntegerField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=200)),
                ("password", models.CharField(max_length=200)),
                ("full_name", models.CharField(max_length=200, null=True)),
                ("address", models.CharField(max_length=200, null=True)),
                ("phone", models.CharField(max_length=200, null=True)),
                ("gender", models.CharField(max_length=200, null=True)),
                ("role", models.CharField(max_length=200)),
                ("is_vip", models.BooleanField()),
            ],
        ),
    ]
