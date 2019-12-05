# Generated by Django 2.2.7 on 2019-12-04 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userConfirmation', '0006_inventario_filename'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_tipouser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userConfirmation.TipoUsuario'),
        ),
    ]