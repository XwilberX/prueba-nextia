# Generated by Django 4.0.3 on 2022-03-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_bienesmodel_id_alter_usermodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bienesmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
