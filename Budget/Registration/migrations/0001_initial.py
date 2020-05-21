# Generated by Django 3.0.3 on 2020-05-06 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymode', models.CharField(max_length=250)),
                ('user', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Essential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='udtl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tel', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('dfield', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.Essential')),
                ('paymode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.Account')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.udtl')),
            ],
        ),
    ]
