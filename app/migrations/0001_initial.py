# Generated by Django 4.2.7 on 2024-02-12 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2080)),
                ('department', models.CharField(max_length=2080)),
                ('dob', models.DateField()),
                ('designation', models.CharField(max_length=2080)),
                ('salary', models.CharField(max_length=2080)),
                ('address', models.CharField(max_length=2080)),
                ('others', models.TextField()),
            ],
        ),
    ]
