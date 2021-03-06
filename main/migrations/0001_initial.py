# Generated by Django 2.2.10 on 2020-03-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('confirm', models.IntegerField(blank=True)),
                ('suspicious', models.BooleanField(blank=True)),
                ('protection', models.CharField(max_length=20)),
                ('status', models.CharField(blank=True, max_length=20)),
                ('text', models.TextField(blank=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Chinese_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chinese_student_Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info_Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='School_Find',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Faculty', models.IntegerField()),
                ('postg', models.IntegerField()),
                ('underg', models.IntegerField()),
            ],
        ),
    ]
