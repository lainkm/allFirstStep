class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self):
    	print('%s' % self.path)

    def __str__(self):
        return self._path   #返回类的信息

    __repr__ = __str__      #调试时返回类的信息


def create():
	print(Chain().status.user.timeline.list)
	print(Chain("niha").repos)

if __name__ == "__main__":
	create()