# Generated by Django 4.1.7 on 2023-04-10 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0003_alter_user_id_user_alter_user_is_vip"),
    ]

    operations = [
        migrations.CreateModel(
            name="History",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("exp_vip", models.CharField(max_length=200)),
                ("is_vip", models.CharField(max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.user"
                    ),
                ),
            ],
        ),
    ]
