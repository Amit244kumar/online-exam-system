# Generated by Django 4.0.4 on 2022-06-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTS', '0002_question_delete_quetion'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=40)),
                ('realname', models.CharField(max_length=20)),
            ],
        ),
    ]
