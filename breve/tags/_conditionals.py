class Switch(object):
    def __init__(self, value):
        self.value = value

    def __getitem__(self, conditions):
        for c in conditions:
            if c.default or (c.value == self.value):
                return c.children
        return ''


class Case(object):
    def __init__(self, value=None, default=False):
        self.default = default
        self.value = value

    def __call__(self, value):
        self.value = value
        return value

    def __getitem__(self, children):
        self.children = children
        return self


default = Case(default=True)


class When(object):
    def __init__(self, condition):
        self.value = bool(condition)

    def __getitem__(self, children):
        if self.value:
            return children
        return ''


if __name__ == '__main__':
    x = 5
    username = 'bob'

    print(Switch(x)[
              Case(1)['x is 1'],
              Case(2)['x is 2'],
              Case(3)['x is 3'],
              default['x is not in list']
          ])

    print(Switch(bool(username))[
              Case(True)['%s is logged in' % username],
              Case(False)['you are not logged in']
          ])

    print(When(x == 5)[
              'x is 5'
          ])
    print(When(x != 4)[
              'x is not 4'
          ])
