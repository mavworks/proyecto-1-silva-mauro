# Generated by Django 4.2.2 on 2023-08-08 00:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_alter_resenia_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infousuario',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
