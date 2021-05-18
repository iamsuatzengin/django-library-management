# Generated by Django 3.2.3 on 2021-05-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0006_alter_author_options'),
        ('accounts', '0003_alter_profile_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='library_app.Book'),
        ),
    ]