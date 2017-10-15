from enum import Enum, unique

#获得Month的枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May'))

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

#精确的控制枚举类型
@unique
class weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

print(weekday.Sun, weekday.Sun.value)
print(weekday(6), weekday(6).value)

