from contextlib import contextmanager


class QueryCls(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager  # 将此方法变为上下文  方便with使用  with方法标志要按顺序吧方法执行完成
def create_query(name):
    print('Begin')
    q = QueryCls(name)
    yield q
    print('End')


with create_query('Bob') as q:
    pass  # 表示往下执行
    # print(q)
    # q.query()

print("---------------------")

with create_query('Bob') as q:
    q.query()
