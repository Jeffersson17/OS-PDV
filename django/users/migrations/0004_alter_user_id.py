# Generated by Django 5.1.2 on 2024-12-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_enterprise"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]