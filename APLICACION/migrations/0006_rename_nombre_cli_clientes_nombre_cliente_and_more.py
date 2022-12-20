# Generated by Django 4.1.2 on 2022-11-30 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APLICACION', '0005_cita_clientes_funcionarios_mascota_raza_tipo_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='nombre_cli',
            new_name='nombre_cliente',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='nom_mas',
            new_name='nombre_mascota',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='rut_f',
            new_name='rut_funcionario',
        ),
        migrations.RenameField(
            model_name='tipo_at',
            old_name='atencion_at',
            new_name='tipo_atencion',
        ),
        migrations.RenameField(
            model_name='tipo_m',
            old_name='atencion_m',
            new_name='tipo_mascota',
        ),
        migrations.AlterField(
            model_name='cita',
            name='mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APLICACION.mascota'),
        ),
    ]
