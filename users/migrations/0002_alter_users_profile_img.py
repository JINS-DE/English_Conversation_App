# Generated by Django 5.0.4 on 2024-04-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="profile_img",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_images/%y/%m/%d/"
            ),
        ),
    ]
