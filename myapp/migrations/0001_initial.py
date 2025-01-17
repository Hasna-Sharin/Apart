# Generated by Django 4.2 on 2023-05-07 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apartmentDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aname', models.CharField(blank=True, max_length=100, null=True)),
                ('Oname', models.CharField(blank=True, max_length=50, null=True)),
                ('Category', models.CharField(blank=True, max_length=60, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('Description', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
