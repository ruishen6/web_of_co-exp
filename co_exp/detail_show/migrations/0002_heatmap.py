# Generated by Django 2.1 on 2018-10-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail_show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='heatmap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geneaccession', models.CharField(max_length=15)),
                ('runid', models.CharField(max_length=12)),
                ('tpm', models.CharField(max_length=20)),
                ('tissue', models.CharField(max_length=15)),
            ],
        ),
    ]
