# Generated by Django 3.0.5 on 2020-04-09 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Elder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('phone', models.CharField(max_length=12)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('mail', models.EmailField(max_length=254)),
                ('elder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('view', models.PositiveSmallIntegerField(choices=[(1, 'Лекция'), (2, 'Лабораторная работа'), (3, 'Практика')])),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('phone', models.CharField(max_length=12)),
                ('mail', models.EmailField(max_length=254)),
                ('department', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subgroup', models.PositiveIntegerField()),
                ('time', models.TimeField()),
                ('day', models.PositiveSmallIntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')])),
                ('even_week', models.BooleanField()),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Cabinet')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Group')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Cabinet')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Group')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveSmallIntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')])),
                ('even_week', models.BooleanField()),
                ('time', models.TimeField()),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Cabinet')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Teacher')),
            ],
        ),
    ]
