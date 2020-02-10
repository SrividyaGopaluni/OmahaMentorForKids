# Generated by Django 2.2.4 on 2020-02-10 23:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_ID', models.CharField(max_length=50)),
                ('mentor_LastName', models.CharField(blank=True, max_length=100)),
                ('mentor_FirstName', models.CharField(max_length=100)),
                ('mentor_email', models.EmailField(max_length=100)),
                ('mentor_address', models.CharField(max_length=200)),
                ('mentor_city', models.CharField(max_length=50)),
                ('mentor_state', models.CharField(max_length=50)),
                ('mentor_zipcode', models.CharField(max_length=10)),
                ('mentor_phone_number', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.CharField(max_length=50)),
                ('student_schoolID', models.CharField(blank=True, max_length=100)),
                ('student_FirstName', models.CharField(max_length=100)),
                ('student_LastName', models.CharField(max_length=100)),
                ('student_gender', models.CharField(max_length=100)),
                ('student_dateofbirth', models.DateTimeField(max_length=50)),
                ('student_email', models.EmailField(max_length=100)),
                ('student_address', models.CharField(max_length=200)),
                ('student_city', models.CharField(max_length=50)),
                ('student_state', models.CharField(max_length=50)),
                ('student_zipcode', models.CharField(max_length=10)),
                ('student_phone_number', models.CharField(max_length=50)),
                ('student_school', models.CharField(max_length=50)),
                ('student_notes', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentMentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_ID', models.CharField(max_length=50)),
                ('group_Name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('mentor_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='mentorapplication.Mentor')),
                ('student_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='mentorapplication.Student')),
            ],
        ),
    ]
