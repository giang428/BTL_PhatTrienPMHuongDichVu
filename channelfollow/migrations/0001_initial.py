# Generated by Django 4.1.7 on 2023-04-14 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0003_alter_user_id_user_alter_user_is_vip"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChannelFollow",
            fields=[
                ("id_follow", models.AutoField(primary_key=True, serialize=False)),
                ("day_follow", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.user"
                    ),
                ),
            ],
        ),
    ]
