# Generated by Django 3.2.7 on 2021-11-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melodic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='cover',
            field=models.CharField(default='No Image', max_length=9999),
        ),
    ]