# Generated by Django 4.2.2 on 2023-08-08 00:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0011_remove_resenia_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resenia',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
