# Generated by Django 4.0.2 on 2022-02-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='meal',
            field=models.TextField(choices=[('Cheeseburger', 10), ('Hot dog', 5), ('Pizza', 7), ('T-Bone', 20), ('French fries', 3), ('Salmon tartar', 15)], max_length=20),
        ),
    ]
