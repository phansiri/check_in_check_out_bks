# Generated by Django 3.1.4 on 2021-01-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cico_app', '0002_person_company_in_battalion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='company_in_battalion',
            field=models.CharField(choices=[('-', 'None'), ('A', 'Alpha'), ('B', 'Bravo'), ('DCO', 'DCO-IDM'), ('HQ', 'Headquarters'), ('SVR', 'Service')], default='-', max_length=3),
        ),
    ]
