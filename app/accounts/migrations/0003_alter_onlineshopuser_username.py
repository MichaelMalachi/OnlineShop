# Generated by Django 5.0.2 on 2024-03-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_onlineshopuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlineshopuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='username'),
        ),
    ]