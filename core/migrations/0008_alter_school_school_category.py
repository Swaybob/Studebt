# Generated by Django 4.0.6 on 2022-07-30 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_category_school_school_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='core.cat'),
        ),
    ]