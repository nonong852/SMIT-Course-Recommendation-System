# Generated by Django 5.0.4 on 2024-04-21 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_tfees', models.IntegerField()),
                ('c_eligibility', models.IntegerField()),
                ('c_description', models.TextField()),
                ('c_rstream', models.CharField(max_length=100)),
                ('c_type', models.CharField(max_length=100)),
                ('c_img', models.ImageField(upload_to='static/courses_pic')),
                ('c_code', models.IntegerField()),
            ],
        ),
    ]
