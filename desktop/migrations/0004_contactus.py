# Generated by Django 2.2.8 on 2019-12-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desktop', '0003_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('mobile', models.CharField(max_length=64, null=True)),
                ('email', models.CharField(max_length=64, null=True)),
                ('facebook', models.CharField(max_length=64, null=True)),
                ('twitter', models.CharField(max_length=64, null=True)),
                ('instgram', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]
