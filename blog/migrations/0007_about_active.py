# Generated by Django 3.1.5 on 2021-01-24 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_contact_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
