# Generated by Django 4.1.7 on 2023-03-01 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout_app', '0002_alter_cats_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cats',
            options={'verbose_name': 'Кот', 'verbose_name_plural': 'Коты'},
        ),
        migrations.AddField(
            model_name='cats',
            name='image',
            field=models.ImageField(blank=True, db_column='Image', null=True, upload_to='layout_app/static/layout_app/img'),
        ),
    ]