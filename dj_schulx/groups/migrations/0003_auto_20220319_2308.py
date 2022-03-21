# Generated by Django 3.2.11 on 2022-03-19 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20220306_2238"),
        ("groups", "0002_auto_20220313_2241"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentpresence",
            name="lesson",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="groups.lesson"
            ),
        ),
        migrations.AlterField(
            model_name="studentpresence",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="users.student"
            ),
        ),
    ]
