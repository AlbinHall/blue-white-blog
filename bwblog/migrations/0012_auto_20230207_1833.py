# Generated by Django 3.2.16 on 2023-02-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwblog', '0011_alter_commentdisc_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdisc',
            name='text',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]