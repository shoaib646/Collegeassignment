# Generated by Django 3.2.23 on 2024-03-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishmarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishmarketmodel',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fishmarketmodel',
            name='length1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fishmarketmodel',
            name='length2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fishmarketmodel',
            name='length3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fishmarketmodel',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fishmarketmodel',
            name='width',
            field=models.FloatField(),
        ),
    ]
