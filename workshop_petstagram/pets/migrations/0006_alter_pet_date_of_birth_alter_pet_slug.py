# Generated by Django 4.1.2 on 2022-10-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_alter_pet_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
