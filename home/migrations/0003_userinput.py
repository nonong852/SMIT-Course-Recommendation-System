# Generated by Django 5.0.4 on 2024-04-25 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_courses_c_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='userinput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField()),
                ('stream', models.CharField(max_length=100)),
                ('budget', models.IntegerField()),
            ],
        ),
    ]