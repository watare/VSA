# Generated by Django 4.1.2 on 2022-10-05 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ovs_conf", "0005_alter_port_ingress_policing_burst_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="port",
            name="mac",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
    ]
