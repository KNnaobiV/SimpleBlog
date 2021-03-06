# Generated by Django 3.1.5 on 2021-01-14 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_about_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
