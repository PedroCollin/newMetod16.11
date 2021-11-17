# Generated by Django 3.2.9 on 2021-11-17 11:32

from django.db import migrations, models
import django.db.models.deletion
import estudo.models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('ativo', models.BooleanField(default=True)),
                ('cargo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('ativo', models.BooleanField(default=True)),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=100)),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Grafico'), ('lni-users', 'Usuarios'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=12)),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=200)),
                ('facebook', models.CharField(default='#', max_length=200, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=200, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=200, verbose_name='Instagram')),
                ('foto', stdimage.models.StdImageField(upload_to=estudo.models.troca_nome, verbose_name='Foto')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudo.cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
            },
        ),
    ]