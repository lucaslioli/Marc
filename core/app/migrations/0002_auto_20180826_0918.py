# Generated by Django 2.1 on 2018-08-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='proceso_interno',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='processo_externo',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='transportadora',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
