# Generated by Django 4.0.4 on 2022-04-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_emp_blog_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='DOB',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='DOJ',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
