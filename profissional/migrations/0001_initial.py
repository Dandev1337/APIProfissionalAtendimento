# Generated by Django 5.0.3 on 2024-03-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('especialidade', models.CharField(default='', max_length=255)),
                ('telefone', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
