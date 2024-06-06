# Generated by Django 4.1.3 on 2022-12-09 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0010_contactinfo_githuburl'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='emailImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='githubUrlImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='hackerrankUrlImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='leetcodeUrlImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='link1Img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='link2Img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='linkedInUrlImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='phoneImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='youtubeUrlImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
