# Generated by Django 5.0.4 on 2024-04-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfichier', '0004_uploadimage_name_alter_uploadimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimage',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='description',
            field=models.TextField(default='Untitled'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
