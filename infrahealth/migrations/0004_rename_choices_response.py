# Generated by Django 3.2.9 on 2022-01-25 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infrahealth', '0003_alter_choices_choice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choices',
            new_name='Response',
        ),
    ]