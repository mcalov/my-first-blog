# Generated by Django 3.0.1 on 2020-02-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_bip_bws_oekonomie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bip',
            name='Einwohner',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bip',
            name='Erwerbstaetiger',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bws',
            name='Einwohner',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bws',
            name='Erwerbstaetiger',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bws',
            name='ErwerbstaetigerLandForstFischerei',
            field=models.IntegerField(null=True),
        ),
    ]
