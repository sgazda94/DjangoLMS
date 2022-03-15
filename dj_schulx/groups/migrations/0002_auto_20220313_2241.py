# Generated by Django 3.2.11 on 2022-03-13 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20220306_2238"),
        ("courses", "0002_alter_lessonscript_course"),
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="courses.course",
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="teacher",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.teacher",
            ),
        ),
    ]