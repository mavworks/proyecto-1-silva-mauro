# Generated by Django 4.2.2 on 2023-07-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_rename_avatar_fotoresenia_foto_resenia'),
    ]

    operations = [
        migrations.AddField(
            model_name='resenia',
            name='foto_resenia',
            field=models.ImageField(blank=True, null=True, upload_to='img_resenias'),
        ),
        migrations.DeleteModel(
            name='FotoResenia',
        ),
    ]