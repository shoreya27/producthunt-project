# Generated by Django 2.2.5 on 2019-09-08 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('url', models.URLField(max_length=20)),
                ('publish_date', models.DateField()),
                ('votes_total', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='')),
                ('icon', models.ImageField(height_field=10, upload_to='', width_field=10)),
                ('body', models.CharField(max_length=200)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
