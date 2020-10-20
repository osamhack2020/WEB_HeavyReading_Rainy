# Generated by Django 2.1 on 2020-10-20 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0011_book_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.SmallIntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Book')),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
