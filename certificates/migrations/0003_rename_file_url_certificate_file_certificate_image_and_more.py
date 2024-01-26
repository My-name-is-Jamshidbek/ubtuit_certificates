# Generated by Django 5.0.1 on 2024-01-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_alter_certificate_file_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='file_url',
            new_name='file',
        ),
        migrations.AddField(
            model_name='certificate',
            name='image',
            field=models.ImageField(default=0, height_field='image_height', upload_to='certificate_images/', width_field='image_width'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificate',
            name='image_height',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='certificate',
            name='image_width',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
