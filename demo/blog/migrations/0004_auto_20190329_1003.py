# Generated by Django 2.1.7 on 2019-03-29 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_author_book_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='0', max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='time',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='author',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='append_publisher', to='blog.Publisher'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='append_book', to='blog.Book'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='book',
            name='color',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
    ]