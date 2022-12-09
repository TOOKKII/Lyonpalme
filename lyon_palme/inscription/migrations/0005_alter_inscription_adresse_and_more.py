# Generated by Django 4.1.4 on 2022-12-09 20:15

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0004_rename_adherants_adherents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='adresse',
            field=django_cryptography.fields.encrypt(models.CharField(help_text='Rentrez votre adresse', max_length=50)),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='autorisation_parentale',
            field=django_cryptography.fields.encrypt(models.ImageField(null=True, upload_to='')),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='certificat_medical',
            field=django_cryptography.fields.encrypt(models.ImageField(null=True, upload_to='')),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='code_postal',
            field=django_cryptography.fields.encrypt(models.IntegerField(help_text='Rentrez votre code postal')),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='date_certificat',
            field=django_cryptography.fields.encrypt(models.DateTimeField(max_length=50, null=True)),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='date_inscription',
            field=django_cryptography.fields.encrypt(models.DateTimeField(max_length=50)),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='date_naissance',
            field=django_cryptography.fields.encrypt(models.DateTimeField(help_text='Rentrez votre date de naissance', max_length=50)),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='fiche_inscription',
            field=django_cryptography.fields.encrypt(models.ImageField(null=True, upload_to='')),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='mail',
            field=django_cryptography.fields.encrypt(models.CharField(help_text='Rentrez votre adresse email', max_length=50)),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='nom',
            field=django_cryptography.fields.encrypt(models.CharField(help_text='Rentrez votre nom', max_length=50)),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='photo',
            field=django_cryptography.fields.encrypt(models.ImageField(null=True, upload_to='')),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='prenom',
            field=django_cryptography.fields.encrypt(models.CharField(help_text='Rentrez votre prénom', max_length=50)),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='telephone',
            field=django_cryptography.fields.encrypt(models.CharField(help_text='Rentrez votre numéro de téléphone', max_length=20)),
        ),
    ]
