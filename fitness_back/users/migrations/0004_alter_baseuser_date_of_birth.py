# Generated by Django 4.2.2 on 2024-04-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_baseuser_role_delete_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
