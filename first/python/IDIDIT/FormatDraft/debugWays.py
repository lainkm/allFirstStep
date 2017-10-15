import logging
import pdb
# logging.basicConfig(level = logging.DEBUG)
# logging.basicConfig(level = logging.INFO)
# logging.basicConfig(level = logging.WARNING)
logging.basicConfig(level = logging.ERROR)

n = 0
logging.debug('n = %d' % n)
logging.info('n = %d' % n)
logging.warning('n = %d' % n)
logging.error('n = %d' % n)
n = 1
logging.debug('n = %d' % n)
logging.info('n = %d' % n)
logging.warning('n = %d' % n)
logging.error('n = %d' % n)
n = 2
logging.debug('n = %d' % n)
logging.info('n = %d' % n)
logging.warning('n = %d' % n)
logging.error('n = %d' % n)


# 设置断点
a, b , c = 2, 3, 4
print(a)
pdb.set_trace()   #p查看，c继续执行，python -m pdb debugWays.py 用n单步执行
print(b)
print(c)
