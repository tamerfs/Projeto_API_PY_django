# Generated by Django 4.1.2 on 2022-10-18 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('provedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aulas', to='provedor.provedor')),
            ],
        ),
    ]
