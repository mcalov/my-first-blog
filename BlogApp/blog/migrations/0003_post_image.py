# Generated by Django 3.0.1 on 2020-01-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191228_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/no-img.jpg', upload_to='images/'),
        ),
    ]