# Generated by Django 4.0.8 on 2023-07-02 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_user_mentororstudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Languages',
            field=models.CharField(choices=[('1', 'Akshay'), ('2', 'Rahit'), ('3', 'Rahul'), ('4', 'Rohit'), ('6', 'Rohan'), ('6', 'Karunß')], default='', max_length=20),
        ),
    ]