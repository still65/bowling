# coding: UTF-8

import argparse
import logging
import texttable as tt
import sys
from parse import Parse
from settings import MAX_RESULT
from frame import Frame

my_logger = logging.getLogger('my')

ex = "8/9-X X 6/4/X 8-X XXX"


class Game(object):

    def __init__(self, string):
        self.string_frames = list(Parse(ex).parse())
        self.string = string
        self.frames = list(self.get_frames())

    def get_frame_result(self):
        fn = 0
        for index, frame in enumerate(self.frames):
            frame.previous_frame = self.frames[index-1]
            if index == 0:
                fn = fn + frame.get_total_score(None)
            else:
                fn = fn + frame.get_total_score(frame.previous_frame)
            my_logger.debug(u'Общее количество набранных очков - {}'.format(fn))
            yield fn

    def get_frames(self):
        line = iter(self.string_frames)
        i = 0
        while line:
            i += 1
            first_throw = line.next()
            first = first_throw[0]
            second = first_throw[1]
            if second == '' or second == '-':
                second = 0
            if first == 'X':
                if i > 9:
                    if second == 'X':
                        second = 10
                    yield Frame(10, int(second))
                    continue
                else:
                    yield Frame(10, 0)
                    continue
            if first == 'XX':
                if i > 9:
                    yield Frame(20, int(second))
                    continue
                yield Frame(20, 0)
            if first == 'XXX':
                first = 30
            elif first == '-':
                first = 0
            else:
                first = int(first)
            if second == '/':
                second = MAX_RESULT - first
            yield Frame(first, int(second))

    def get_final_result(self):
        game = Game(ex)
        parse = Parse(ex)
        gen = list(parse.parse())
        l1 = [x for x in gen]
        list_frames = []
        for q in l1:
            list_frames.append(q[0] + q[1])
        t = tt.Texttable()
        header = ['1', '2', '3', '4',  '5', '6', '7', '8', '9', '10']
        t.header(header)
        row = list_frames
        if len(row) < 10:
            raise Exception('Введены некорректные данные, строка слишком короткая!')
        t.add_row(row)
        row = list(game.get_frame_result())
        t.add_row(row)
        t.set_chars(['-', '|', '+', '='])
        s = t.draw()

        return s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', default=ex)
    namespace = parser.parse_args(sys.argv[1:])

    game = Game(namespace.r)
    result = game.get_final_result()

    print result

if __name__ == '__main__':
        main()
