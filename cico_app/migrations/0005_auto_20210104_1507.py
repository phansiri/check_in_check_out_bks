# Generated by Django 3.1.4 on 2021-01-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cico_app', '0004_auto_20210103_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='company_in_battalion',
            field=models.CharField(choices=[('-', '---'), ('A', 'Alpha'), ('B', 'Bravo'), ('DCO', 'DCO-IDM'), ('HQ', 'Headquarters'), ('SVC', 'Service')], default='-', max_length=3),
        ),
    ]