# coding: UTF-8
import logging

from throw import Throw
from settings import MAX_RESULT


my_logger = logging.getLogger('my')


class Frame(object):

    def __init__(self, first_throw, second_throw):
        self.first_throw = Throw(self, first_throw)
        self.second_throw = Throw(self, second_throw)
        self.previous_frame = None

    @property
    def strike(self):
        return self.first_throw.knocked_off == MAX_RESULT

    @property
    def spare(self):
        return not self.strike and self.first_throw.knocked_off + self.second_throw.knocked_off == MAX_RESULT

    def get_total_score(self, prev_fr):
        score = self.first_throw.knocked_off
        score += self.second_throw.knocked_off
        if prev_fr:
            if prev_fr.first_throw.knocked_off == 10:
                score += self.first_throw.knocked_off + self.second_throw.knocked_off
            elif prev_fr.first_throw.knocked_off + prev_fr.second_throw.knocked_off == 10:
                score += self.first_throw.knocked_off
        my_logger.debug(u'Общий счет броска {}'.format(score))
        return score
