# Generated by Django 4.1.1 on 2022-10-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0003_remove_trait_animals'),
        ('animals', '0003_rename_scientific_name_animal_group_alter_animal_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='traits',
            field=models.ManyToManyField(related_name='trait', to='traits.trait'),
        ),
    ]
