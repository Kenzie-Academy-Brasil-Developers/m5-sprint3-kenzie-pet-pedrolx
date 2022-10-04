# Generated by Django 4.1.1 on 2022-10-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('animals', models.ManyToManyField(related_name='trait_names', to='animals.animal')),
            ],
        ),
    ]
