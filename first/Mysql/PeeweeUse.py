from peewee import *

database = MySQLDatabase('Web_db', **{'host': 'localhost', 'password': \
                              '666666','user':'root'})
database.connect()

print(database.get_conn())


class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class SyShieldOrder(BaseModel):
    _id = PrimaryKeyField()
    order_up_day = IntegerField(null=True)
    order_up_hours = IntegerField(null=True)
    order_up_moon = IntegerField(null=True)
    order_up_quarter = IntegerField(null=True)
    order_up_week = IntegerField(null=True)
    order_up_year = IntegerField(null=True)
    tu_shopid = CharField(null=True)

    class Meta:
        db_table = 'sy_shield_order'

class SyShieldUser(BaseModel):
    _id = PrimaryKeyField()
    tu_account = CharField(null=True)
    tu_area = CharField(null=True)
    tu_city = CharField(null=True)
    tu_commence = DateField(null=True)
    tu_contract = DateField(null=True)
    tu_cost = IntegerField(null=True)
    tu_domain = CharField(null=True)
    tu_nick = CharField(null=True)
    tu_platform = CharField(null=True)
    tu_province = CharField(null=True)
    tu_realcost = IntegerField(null=True)
    tu_shopid = CharField(null=True)
    tu_version = CharField(null=True)

    class Meta:
        db_table = 'sy_shield_user'


from datetime import datetime
from src import *

database.connect()

for i in SyShieldUser.select():
    print i.tu_account
    print i.__dict__

for i in range(10):
    data = {
        'tu_account': "user_%s" % str(i),
        'tu_area': "HuaDong",
        'tu_city': "Shanghai",
    }
print SyShildUser.create(tu_account="user", tu_area="HuaDong", tu_city="Shanghai", tu_shopid="100000%s" % str(i))
