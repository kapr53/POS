# Generated by Django 3.2.9 on 2021-11-16 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('registration', '0006_auto_20211116_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cui',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='CUI'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, verbose_name='Genero'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Telefono'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('0', 'Gerente'), ('1', 'Administrador'), ('2', 'Vendedor')], default=2, null=True, verbose_name='Rol'),
        ),
        migrations.AddField(
            model_name='user',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
