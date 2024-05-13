# Generated by Django 5.0.6 on 2024-05-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32, verbose_name="书籍名称")),
                ("owned_date", models.DateField(verbose_name="拥有日期")),
                (
                    "current_position",
                    models.CharField(max_length=255, verbose_name="当前存储位置(描述)"),
                ),
                (
                    "reading_process",
                    models.CharField(max_length=255, verbose_name="阅读进程(描述)"),
                ),
                ("readings", models.IntegerField(default=0, verbose_name="阅读次数")),
                (
                    "remove_status",
                    models.BooleanField(default=False, verbose_name="移除状态"),
                ),
            ],
            options={
                "verbose_name": "书",
                "verbose_name_plural": "书",
                "db_table": "book",
            },
        ),
    ]
