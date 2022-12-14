# Generated by Django 4.1.2 on 2022-10-05 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ovs_conf", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OtherBridgeConfig",
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
                ("other_config", models.CharField(max_length=50)),
                (
                    "bridge",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ovs_conf.ovsbridges",
                    ),
                ),
            ],
        ),
    ]
