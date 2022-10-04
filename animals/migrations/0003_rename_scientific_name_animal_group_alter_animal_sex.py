# Generated by Django 4.1.1 on 2022-10-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_rename_group_scientific_name_animal_scientific_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='scientific_name',
            new_name='group',
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('Macho', 'Male'), ('Fêmea', 'Female'), ('Não Informado', 'Uninformed')], default='Não Informado', max_length=15),
        ),
    ]