# Generated by Django 5.2 on 2025-05-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('clas', models.IntegerField()),
                ('section', models.CharField(max_length=1)),
                ('book_title', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
