# Generated by Django 3.2.20 on 2023-08-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_callbooking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbooking',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]