# Generated by Django 3.2.3 on 2021-05-18 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_app', '0008_alter_bookcomments_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcomments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
