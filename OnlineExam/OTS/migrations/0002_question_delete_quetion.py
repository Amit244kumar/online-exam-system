# Generated by Django 4.0.4 on 2022-05-31 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('que_no', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('que', models.CharField(max_length=200)),
                ('optiona', models.CharField(max_length=100)),
                ('optionb', models.CharField(max_length=100)),
                ('optionc', models.CharField(max_length=100)),
                ('optiond', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Quetion',
        ),
    ]
