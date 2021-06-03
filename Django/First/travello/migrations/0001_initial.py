# Generated by Django 3.2.3 on 2021-06-01 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
