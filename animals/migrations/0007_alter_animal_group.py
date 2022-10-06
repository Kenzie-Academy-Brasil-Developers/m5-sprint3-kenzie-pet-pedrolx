# Generated by Django 4.1.1 on 2022-10-06 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('animals', '0006_alter_animal_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='groups.group'),
        ),
    ]