# Generated by Django 3.2.8 on 2022-10-26 22:18

from django.db import migrations
import manager.fields


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_topping_topping_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topping',
            old_name='topping_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=manager.fields.CaseInsensitiveCharField(max_length=100, null=True),
        ),
    ]
