# Generated by Django 5.0.6 on 2024-08-01 13:35

import PosBack.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('fname', models.CharField(max_length=200)),
                ('zname', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('extra_name', models.CharField(max_length=1000)),
                ('edes', models.CharField(max_length=1000, null=True)),
                ('ldes', models.CharField(max_length=1000, null=True)),
                ('fdes', models.CharField(max_length=1000, null=True)),
                ('des', models.CharField(max_length=1000, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=PosBack.models.get_upload_path_category)),
                ('color', models.CharField(default='rgb(255, 255, 255)', max_length=100)),
                ('text_color', models.CharField(default='rgb(0, 0, 0)', max_length=100)),
                ('time_supply', models.IntegerField()),
                ('Xu_class', models.CharField(db_column='Xu_class', max_length=200, null=True)),
                ('rid', models.IntegerField(default=0)),
                ('category_class', models.IntegerField(default=0)),
                ('sort_id', models.IntegerField(default=0)),
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
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
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
                ('id_printer', models.IntegerField()),
                ('printer', models.CharField(db_comment='print to where list id', max_length=1000)),
                ('rid', models.IntegerField()),
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
                ('id_user', models.CharField(max_length=100, unique=True)),
                ('id_Xu', models.CharField(db_column='id_Xu', max_length=100)),
                ('ename', models.CharField(max_length=200, null=True)),
                ('lname', models.CharField(max_length=200, null=True)),
                ('fname', models.CharField(max_length=200, null=True)),
                ('zname', models.CharField(max_length=200, null=True)),
                ('online_content', models.CharField(max_length=200, null=True)),
                ('bill_content', models.CharField(max_length=100)),
                ('kitchen_content', models.CharField(max_length=200, null=True)),
                ('extra_name', models.CharField(max_length=1000, null=True)),
                ('edes', models.CharField(max_length=1000, null=True)),
                ('ldes', models.CharField(max_length=1000, null=True)),
                ('fdes', models.CharField(max_length=1000, null=True)),
                ('online_des', models.CharField(max_length=1000, null=True)),
                ('allergen', models.CharField(max_length=1000, null=True)),
                ('discount', models.CharField(max_length=200, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=PosBack.models.get_upload_path_product)),
                ('color', models.CharField(default='rgb(255, 255, 255)', max_length=100)),
                ('text_color', models.CharField(default='rgb(0, 0, 0)', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('price2', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('price_extra', models.CharField(max_length=2000, null=True)),
                ('extra_TVA', models.DecimalField(db_column='extra_TVA', decimal_places=2, default=0, max_digits=8)),
                ('time_supply', models.IntegerField(db_comment='1:lunch,2:dinner,12:allday', default=12)),
                ('product_type', models.IntegerField(db_comment='product/set/option', default=0)),
                ('dinein_takeaway', models.IntegerField(db_comment='1=dine-in, 2=takeaway', default=1)),
                ('soldout', models.IntegerField(default=0)),
                ('min_nbr', models.IntegerField(db_comment='minimum purchase nbr', default=1)),
                ('rid', models.IntegerField(db_comment='restaurant id', default=0)),
                ('stb', models.IntegerField(db_comment='sushi to bar', null=True)),
                ('position', models.IntegerField(default=0)),
                ('favourite', models.IntegerField(default=0)),
                ('follow_id', models.IntegerField(default=0)),
                ('extra_id', models.IntegerField(default=0)),
                ('Xu_class', models.CharField(db_column='Xu_class', max_length=200, null=True)),
                ('cut_group', models.IntegerField(null=True)),
                ('custom', models.CharField(db_comment='customisation', max_length=200, null=True)),
                ('custom2', models.CharField(db_comment='customisation 2', max_length=200, null=True)),
                ('custom3', models.CharField(max_length=200, null=True)),
                ('custom4', models.CharField(max_length=200, null=True)),
                ('custom5', models.CharField(max_length=200, null=True)),
                ('print_to_where', models.IntegerField(db_column='print_to_where', default=1)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'testforeignkey',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='tva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryEnglish', models.CharField(max_length=100)),
                ('countryChinese', models.CharField(max_length=100)),
                ('countryFrench', models.CharField(max_length=100)),
                ('countryDutch', models.CharField(max_length=100)),
                ('category', models.IntegerField()),
                ('tva_value', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'tva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/test_images/%Y/%m')),
            ],
            options={
                'db_table': 'testimg',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('country', models.CharField(choices=[('Belgium', 'Belgium'), ('France', 'France')], default='Belgium', max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
