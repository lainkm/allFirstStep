from peewee import *
from datetime import date

db = MySQLDatabase('mydb', **{'host': 'localhost', 'password': \
'666666','user':'root'})
db.connect()
print(db.get_conn())

class BaseModel(Model):
    class Meta:
        database = db;

class Personp(BaseModel):
    name = CharField()
    birthday = DateField()

class Petp(BaseModel):
    name = CharField()
    owner = ForeignKeyField(Personp, related_name = 'pets')

db.create_tables([Personp, Petp])
uncle_Bob = Personp(name = 'Bob', birthday = date(1960,4,15))
uncle_Bob.save()
grandma = Personp.create(name='Grandma', birthday=date(1935, 3, 1))
herb = Personp.create(name='Herb', birthday=date(1950, 5, 5))

# 通过属性改
grandma.name = 'Jane'

bob_kitty = Petp.create(owner=uncle_Bob, name='Kitty')
herb_fido = Petp.create(owner=herb, name='Fido')
herb_mittens = Petp.create(owner=herb, name='Mittens')
herb_mittens_jr = Petp.create(owner=herb, name='Mittens Jr')

herb_mittens.delete_instance()
herb_fido.owner = uncle_Bob
herb_fido.save()
bob_fido = herb_fido

# 获取列表数据
for person in Personp.select():
    print("name",person.name, person.birthday)

query = Petp.select().where(Petp.owner.name == 'herb')
for pet in query:
    print('name',pet.name, "and owner name",pet.owner.name)

# 连接查询
query = (Petp.select(Petp,Personp).join(Personp).where(Petp.owner.name == 'herb'))
for pet in query:
    print(pet.name, pet.owner.name)



db.close()



