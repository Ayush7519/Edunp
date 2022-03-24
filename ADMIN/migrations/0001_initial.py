# Generated by Django 4.0.2 on 2022-03-24 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CATEGORY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SUBJECT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Subject_Code', models.IntegerField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADMIN.category')),
            ],
        ),
        migrations.CreateModel(
            name='UNIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADMIN.category')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADMIN.subject')),
            ],
        ),
        migrations.CreateModel(
            name='SUB_TOPICS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic_Name', models.CharField(max_length=100)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADMIN.category')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADMIN.subject')),
                ('Unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADMIN.unit')),
            ],
        ),
    ]