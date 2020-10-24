# Generated by Django 2.1 on 2020-10-07 14:07

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_remove_book_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=imagekit.models.fields.ProcessedImageField(upload_to='images/'),
        ),
    ]