# Generated by Django 4.1.3 on 2022-12-04 14:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_otpcode_otpcodeadmin"),
    ]

    operations = [
        migrations.DeleteModel(
            name="OtpCodeAdmin",
        ),
    ]
