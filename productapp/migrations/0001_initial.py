# Generated by Django 5.0.1 on 2024-01-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pmfdt', models.DateField()),
                ('pexpdt', models.DateField()),
            ],
        ),
    ]