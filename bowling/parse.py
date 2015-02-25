# coding: UTF-8


class Parse(object):

    def __init__(self, string):
        self.string = string

    def parse(self):
        res = filter(lambda x: x.strip(' '), self.string)
        line = iter(res)
        i = 0
        while line:
            i = i +1
            first = line.next()
            if first == 'X':
                if i > 9:
                    f = line.next()
                    try:
                        last = line.next()
                        if not f == 'X':
                            raise Exception('Ошибка ввода, так как 11 бросок не является strike, 12й бросок невозможен')
                        if last == 'X':
                            yield 'XXX', ''
                        else:
                            yield 'XX', last
                    except StopIteration:
                        yield 'X', f
                else:
                    yield 'X', ''
                    continue
            if line:
                second = line.next()
            else:
                second = ''
            if first:
                first = str(first)
            if second:
                second = str(second)
            if first == '/':
                raise Exception('Ошибка, проверьте правильность ввода, ошибочный Frame №{}!'.format(i))
            if second == 'X':
                raise Exception('Ошибка, проверьте правильность ввода ошибочный Frame №{}!'.format(i))
            first = str(first)
            second = str(second)
            yield first, second

