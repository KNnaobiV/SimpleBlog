# Generated by Django 3.1.5 on 2021-01-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210124_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]