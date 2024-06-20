# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    ename = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    zname = models.CharField(max_length=200)
    extra_name = models.CharField(max_length=1000)
    edes = models.CharField(max_length=1000)
    ldes = models.CharField(max_length=1000)
    fdes = models.CharField(max_length=1000)
    img = models.CharField(max_length=200)
    time_supply = models.IntegerField()
    rid = models.IntegerField()
    category_class = models.IntegerField()
    sort_id = models.IntegerField()
    custom = models.CharField(max_length=200)
    custom1 = models.CharField(max_length=200)
    custom2 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'category'


class Choice(models.Model):
    pid = models.IntegerField(db_comment='product ID')
    choicetype = models.ForeignKey('Choicetype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'choice'


class Choicetype(models.Model):
    edes = models.CharField(max_length=1000)
    ldes = models.CharField(max_length=1000)
    fdes = models.CharField(max_length=1000)
    min = models.IntegerField()
    max = models.IntegerField()
    required = models.IntegerField()
    option_list = models.ForeignKey('OptionList', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'choicetype'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OptionList(models.Model):
    rid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'option_list'


class PrinteToWhere(models.Model):
    printer = models.CharField(max_length=1000, db_comment='print to where list id')
    cutgroup = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'printe_to_where'


class Product(models.Model):
    id_user = models.CharField(unique=True, max_length=100)
    id_xu = models.CharField(db_column='id_Xu', unique=True, max_length=100)  # Field name made lowercase.
    ename = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    zname = models.CharField(max_length=200)
    online_content = models.CharField(max_length=200)
    bill_content = models.CharField(max_length=100)
    kitchen_content = models.CharField(max_length=200)
    extra_name = models.CharField(max_length=1000)
    edes = models.CharField(max_length=1000)
    ldes = models.CharField(max_length=1000)
    fdes = models.CharField(max_length=1000)
    bill_des = models.CharField(max_length=1000)
    img = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    price2 = models.DecimalField(max_digits=8, decimal_places=2)
    price_extra = models.CharField(max_length=2000)
    extra_tva = models.DecimalField(db_column='extra_TVA', max_digits=8, decimal_places=2)  # Field name made lowercase.
    time_supply = models.IntegerField(db_comment='1：lunch，2：dinner，12：allday')
    product_type = models.IntegerField(db_comment='product/set/option')
    soldout = models.IntegerField()
    min_nbr = models.IntegerField(db_comment='minimum purchase nbr')
    rid = models.IntegerField(db_comment='restaurant id')
    stb = models.IntegerField(db_comment='sushi to bar')
    position = models.IntegerField()
    favourite = models.IntegerField()
    follow_id = models.IntegerField()
    extra_id = models.IntegerField()
    xu_class = models.CharField(db_column='Xu_class', max_length=200)  # Field name made lowercase.
    custom = models.CharField(max_length=200, db_comment='customisation')
    custom2 = models.CharField(max_length=200, db_comment='customisation 2')
    custom3 = models.CharField(max_length=200)
    custom4 = models.CharField(max_length=200)
    custom5 = models.CharField(max_length=200)
    print_to_where = models.ForeignKey(PrinteToWhere, models.DO_NOTHING, db_column='print_to_where')
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid', db_comment='category')
    option = models.ForeignKey(OptionList, models.DO_NOTHING)
    tva = models.ForeignKey('Tva', models.DO_NOTHING, db_column='TVA_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Test(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    des = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'test'


class Testforeignkey(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.IntegerField()
    foreignkey_name = models.ForeignKey(Test, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'testforeignkey'


class Tva(models.Model):
    countryenglish = models.CharField(db_column='countryEnglish', max_length=100)  # Field name made lowercase.
    countrychinese = models.CharField(db_column='countryChinese', max_length=1000)  # Field name made lowercase.
    countryfrench = models.CharField(db_column='countryFrench', max_length=1000)  # Field name made lowercase.
    countrydutch = models.CharField(db_column='countryDutch', max_length=1000)  # Field name made lowercase.
    category = models.IntegerField()
    tva_value = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tva'
        unique_together = (('countryenglish', 'countrychinese', 'countryfrench', 'countrydutch', 'category'),)
