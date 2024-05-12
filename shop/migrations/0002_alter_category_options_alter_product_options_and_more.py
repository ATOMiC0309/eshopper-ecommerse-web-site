# Generated by Django 5.0.3 on 2024-05-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': '1. Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-pk'], 'verbose_name_plural': '3. Products'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['name'], 'verbose_name_plural': '2. Subcategories'},
        ),
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]