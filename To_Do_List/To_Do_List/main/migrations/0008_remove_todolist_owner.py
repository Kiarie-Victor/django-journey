# Generated by Django 4.2.3 on 2023-07-24 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_items_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='owner',
        ),
    ]