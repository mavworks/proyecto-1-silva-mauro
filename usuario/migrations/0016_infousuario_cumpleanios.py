# Generated by Django 4.2.2 on 2023-08-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0015_remove_infousuario_cumpleanios'),
    ]

    operations = [
        migrations.AddField(
            model_name='infousuario',
            name='cumpleanios',
            field=models.DateField(blank=True, null=True),
        ),
    ]
