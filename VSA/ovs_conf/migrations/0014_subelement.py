# Generated by Django 4.1.2 on 2022-10-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ovs_conf", "0013_delete_vm"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubElement",
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
            ],
        ),
    ]
