# Generated by Django 4.1.7 on 2023-04-15 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_certificate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
