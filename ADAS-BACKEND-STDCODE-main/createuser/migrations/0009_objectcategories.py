# Generated by Django 3.2.4 on 2021-07-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createuser', '0008_assigntaskfiles_project_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objectcategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_category', models.TextField(blank=True, null=True)),
            ],
        ),
    ]