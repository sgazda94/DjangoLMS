# Generated by Django 3.2.11 on 2022-03-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20220306_2238"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
