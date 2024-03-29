# Generated by Django 4.2.2 on 2023-08-07 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_course_class_quantity_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='Alumno Regular'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('present', models.BooleanField(blank=True, default=False, null=True, verbose_name='Presente')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Cursos')),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'estudiantes'}, on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to=settings.AUTH_USER_MODEL, verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Asistencia',
                'verbose_name_plural': 'Asistencias',
            },
        ),
    ]
