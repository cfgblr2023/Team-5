# Generated by Django 4.0.8 on 2023-07-01 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_student_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Languages',
            field=models.CharField(choices=[('1', 'Kannada'), ('2', 'English'), ('3', 'Hindi')], default='Kannada', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='education',
            field=models.CharField(choices=[('1', 'Diploma'), ('2', 'Btech'), ('3', 'High School'), ('4', 'PUC')], default='Diploma', max_length=20),
        ),
    ]
