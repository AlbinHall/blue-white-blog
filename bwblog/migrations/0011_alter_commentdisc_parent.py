# Generated by Django 3.2.16 on 2023-02-04 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bwblog', '0010_alter_commentdisc_discussion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdisc',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='bwblog.commentdisc'),
        ),
    ]
