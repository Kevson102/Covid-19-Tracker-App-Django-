# Generated by Django 3.2.9 on 2022-01-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrahealth', '0011_alter_answer_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.BooleanField(),
        ),
    ]