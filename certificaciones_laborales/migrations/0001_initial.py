# Generated by Django 3.2.6 on 2022-09-30 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificacionLaboral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contrato', models.CharField(max_length=50)),
                ('salario_mensual', models.FloatField()),
                ('empresa_asociada', models.CharField(max_length=50)),
                ('lugar', models.CharField(max_length=50)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.documento')),
            ],
        ),
    ]