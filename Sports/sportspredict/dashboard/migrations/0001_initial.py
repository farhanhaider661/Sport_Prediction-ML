# Generated by Django 4.0.6 on 2022-07-15 07:17

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
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.PositiveBigIntegerField(null=True)),
                ('height', models.PositiveBigIntegerField(null=True)),
                ('sex', models.CharField(choices=[(0, 'Female'), (1, 'Male')], max_length=10, null=True)),
                ('predictions', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]