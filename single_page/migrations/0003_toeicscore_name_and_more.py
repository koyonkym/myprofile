# Generated by Django 5.0.3 on 2024-03-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_page', '0002_alter_toeicscore_administration_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='toeicscore',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='toeicscore',
            name='administration_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='toeicscore',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='toeicscore',
            name='institution_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='toeicscore',
            name='institution_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='toeicscore',
            name='l_percentile_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='toeicscore',
            name='r_percentile_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='toeicscore',
            name='registration_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]