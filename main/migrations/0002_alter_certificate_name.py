# Generated by Django 4.1.7 on 2023-04-15 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
