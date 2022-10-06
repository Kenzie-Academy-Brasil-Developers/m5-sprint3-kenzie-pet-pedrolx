# Generated by Django 4.1.1 on 2022-10-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0003_remove_trait_animals'),
        ('animals', '0004_animal_traits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='traits',
            field=models.ManyToManyField(related_name='traits', to='traits.trait'),
        ),
    ]