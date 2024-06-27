# Generated by Django 5.0.6 on 2024-06-21 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('fname', models.CharField(max_length=200)),
                ('zname', models.CharField(max_length=200)),
                ('extra_name', models.CharField(max_length=1000)),
                ('edes', models.CharField(max_length=1000)),
                ('ldes', models.CharField(max_length=1000)),
                ('fdes', models.CharField(max_length=1000)),
                ('img', models.CharField(max_length=200)),
                ('time_supply', models.IntegerField()),
                ('rid', models.IntegerField()),
                ('category_class', models.IntegerField()),
                ('sort_id', models.IntegerField()),
                ('custom', models.CharField(max_length=200)),
                ('custom1', models.CharField(max_length=200)),
                ('custom2', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(db_comment='product ID')),
            ],
            options={
                'db_table': 'choice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='choicetype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edes', models.CharField(max_length=1000)),
                ('ldes', models.CharField(max_length=1000)),
                ('fdes', models.CharField(max_length=1000)),
                ('min', models.IntegerField()),
                ('max', models.IntegerField()),
                ('required', models.IntegerField()),
            ],
            options={
                'db_table': 'choicetype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='option_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.IntegerField()),
            ],
            options={
                'db_table': 'option_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='printe_to_where',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printer', models.CharField(db_comment='print to where list id', max_length=1000)),
                ('cutgroup', models.IntegerField()),
            ],
            options={
                'db_table': 'printe_to_where',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(default=0)),
                ('id_Xu', models.IntegerField(db_column='id_Xu', default=0)),
                ('ename', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('fname', models.CharField(max_length=200)),
                ('zname', models.CharField(max_length=200)),
                ('print_name', models.CharField(max_length=100)),
                ('extra_name', models.CharField(max_length=1000)),
                ('edes', models.CharField(max_length=1000)),
                ('ldes', models.CharField(max_length=1000)),
                ('fdes', models.CharField(max_length=1000)),
                ('img', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('price2', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('price_extra', models.CharField(max_length=2000)),
                ('TVA_country', models.CharField(db_column='TVA_country', max_length=200)),
                ('TVA', models.DecimalField(db_column='TVA', decimal_places=2, default=0, max_digits=8)),
                ('extra_TVA', models.DecimalField(db_column='extra_TVA', decimal_places=2, default=0, max_digits=8)),
                ('time_supply', models.IntegerField(db_comment='supply time', default=0)),
                ('product_type', models.IntegerField(db_comment='product/set/option', default=0)),
                ('soldout', models.IntegerField(default=0)),
                ('min_nbr', models.IntegerField(db_comment='minimum purchase nbr', default=0)),
                ('rid', models.IntegerField(db_comment='restaurant id', default=0)),
                ('stb', models.IntegerField(db_comment='sushi to bar', default=0)),
                ('position', models.IntegerField(default=0)),
                ('favourite', models.IntegerField(default=0)),
                ('follow_id', models.IntegerField(default=0)),
                ('extra_id', models.IntegerField(default=0)),
                ('xu_class', models.CharField(db_column='Xu_class', max_length=200)),
                ('custom', models.CharField(db_comment='customisation', max_length=200)),
                ('custom2', models.CharField(db_comment='customisation 2', max_length=200)),
                ('custom3', models.CharField(max_length=200)),
                ('custom4', models.CharField(max_length=200)),
                ('custom5', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('des', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Testforeignkey',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'testforeignkey',
                'managed': False,
            },
        ),
    ]
