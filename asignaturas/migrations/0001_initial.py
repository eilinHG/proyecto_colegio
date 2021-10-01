# Generated by Django 3.2.7 on 2021-09-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('area', models.TextField()),
                ('grado', models.CharField(max_length=50)),
                ('docente', models.CharField(max_length=200)),
            ],
        ),
    ]
