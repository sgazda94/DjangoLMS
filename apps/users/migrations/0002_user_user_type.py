# Generated by Django 3.2.11 on 2022-02-21 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_type",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "guardian"),
                    (2, "teacher"),
                    (3, "manager"),
                    (4, "superuser"),
                ],
                null=True,
            ),
        ),
    ]
