# Generated by Django 4.1.3 on 2022-12-08 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0007_delete_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderName', models.CharField(max_length=200)),
                ('senderEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('theMessage', models.TextField()),
            ],
        ),
    ]
