# Generated by Django 5.0.6 on 2024-07-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PosBack', '0007_alter_testimg_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ablist_kitchen_nonull',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Xu_class', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'ablist_kitchen_nonull',
                'managed': False,
            },
        ),
    ]
