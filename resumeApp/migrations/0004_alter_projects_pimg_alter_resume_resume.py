# Generated by Django 4.1.3 on 2022-12-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0003_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='pImg',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.FileField(upload_to=''),
        ),
    ]
