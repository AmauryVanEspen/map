# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('latitud', models.FloatField(default=0)),
                ('longitud', models.FloatField(default=0)),
            ],
            options={
                'ordering': ('provincia', 'nombre'),
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(max_length=300)),
                ('latitud', models.FloatField(default=0)),
                ('longitud', models.FloatField(default=0)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('celular', models.CharField(blank=True, max_length=100, null=True)),
                ('convencional', models.CharField(blank=True, max_length=100, null=True)),
                ('publicada', models.BooleanField(default=False)),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mapae.Ciudad')),
            ],
            options={
                'verbose_name': 'Compa\xf1ia',
                'verbose_name_plural': 'Compa\xf1ias',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('latitud', models.FloatField(default=0)),
                ('longitud', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('latitud', models.FloatField(default=0)),
                ('longitud', models.FloatField(default=0)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapae.Pais')),
            ],
            options={
                'ordering': ('pais', 'nombre'),
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='TipoCompania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('imagen', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Tipo de compa\xf1ia',
                'verbose_name_plural': 'Tipos de compa\xf1ias',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tipocompania',
            unique_together=set([('nombre',)]),
        ),
        migrations.AlterUniqueTogether(
            name='pais',
            unique_together=set([('nombre',)]),
        ),
        migrations.AddField(
            model_name='compania',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapae.Pais'),
        ),
        migrations.AddField(
            model_name='compania',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapae.Provincia'),
        ),
        migrations.AddField(
            model_name='compania',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapae.TipoCompania'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapae.Provincia'),
        ),
        migrations.AlterUniqueTogether(
            name='provincia',
            unique_together=set([('pais', 'nombre')]),
        ),
        migrations.AlterUniqueTogether(
            name='ciudad',
            unique_together=set([('provincia', 'nombre')]),
        ),
    ]