# Generated by Django 2.0.7 on 2018-08-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos_api', '0004_auto_20180813_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedores',
            name='produtos',
        ),
        migrations.AddField(
            model_name='fornecedores',
            name='produtos',
            field=models.ManyToManyField(related_name='fornecedores', to='produtos_api.Produtos'),
        ),
    ]
