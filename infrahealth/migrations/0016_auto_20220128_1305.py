# Generated by Django 3.2.9 on 2022-01-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrahealth', '0015_medicaltest_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicaltest',
            old_name='date',
            new_name='date_tested',
        ),
        migrations.AddField(
            model_name='answer',
            name='date_tested',
            field=models.DateTimeField(auto_now=True),
        ),
    ]