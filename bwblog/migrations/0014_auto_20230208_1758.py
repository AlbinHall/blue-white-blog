# Generated by Django 3.2.16 on 2023-02-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwblog', '0013_likedislike'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='discussion',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='LikeDislike',
        ),
    ]
