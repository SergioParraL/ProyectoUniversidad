# Generated by Django 3.1.6 on 2022-05-31 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registros', '0002_auto_20211104_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='cedula',
            field=models.CharField(max_length=22, unique=True),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='EST/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='personaladm',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='PerAD/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='personaldocente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='PerDO/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='representantes',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='REP/%Y/%m/%d/'),
        ),
    ]
