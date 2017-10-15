import sys
import random
#外部传递参数
print(sys.argv[0])
# print(sys.argv[1])

#

d = ['^','-', '~', '_', '.']
i = random.randint(0, len(d)-1)
print(d[i])
print(random.sample(d, 1))

_str = ''
c = 's'
_str = "{}{}".format(_str,c)
print(_str)