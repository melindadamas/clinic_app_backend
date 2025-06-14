# Generated by Django 5.2.1 on 2025-05-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('descricao', models.CharField(max_length=255)),
                ('categoria_principal', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_categoria', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Ocupação',
                'verbose_name_plural': 'Ocupações',
            },
        ),
    ]
