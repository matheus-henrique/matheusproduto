# Generated by Django 2.0.7 on 2018-08-13 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos_api', '0003_auto_20180813_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='produtos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='produtos_api.Produtos'),
        ),
    ]
