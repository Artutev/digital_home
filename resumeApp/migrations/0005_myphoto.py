# Generated by Django 4.1.3 on 2022-12-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0004_alter_projects_pimg_alter_resume_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selfImage', models.ImageField(upload_to='')),
            ],
        ),
    ]