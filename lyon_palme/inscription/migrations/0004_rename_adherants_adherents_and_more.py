# Generated by Django 4.1.3 on 2022-11-30 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0003_alter_inscription_autorisation_parentale_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adherants',
            new_name='Adherents',
        ),
        migrations.RenameField(
            model_name='categorie',
            old_name='idAdherant',
            new_name='idAdherent',
        ),
        migrations.RenameField(
            model_name='statut',
            old_name='idAdherant',
            new_name='idAdherent',
        ),
    ]
