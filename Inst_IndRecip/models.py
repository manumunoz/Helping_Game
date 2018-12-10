from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import itertools

author = 'Manu Munoz'

doc = """
Indirect Reciprocity - Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'Inst_IndRecip'
    players_per_group = None
    num_rounds = 1
    chosen_rounds = 10
    min_pay = 5
    keep_a = 2
    keep_b = 0
    give_a = 0
    give_b = 5
    history = 3
    exchange = 2
    bonus = 1000
    instructions_template = 'Inst_IndRecip/Instructions.html'

class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle([1, 2, 3]) #1: Full, 2:Sticky, 3:Blind
        # for p in self.get_players():
        #     p.treat = next(treat)
        for p in self.get_players():
            if 'treatment' in self.session.config:
                # demo mode
                p.treat = self.session.config['treatment']
            else:
                # live experiment mode
                p.treat = next(treat)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treat = models.IntegerField() # Treatments from 1 to 3

    symbol = models.PositiveIntegerField(
        choices=[
            [1, 'They are fixed and do not change'],
            [2, 'The computer changes them in each round'],
            [3, 'I can change them in each round'],
        ],
        widget=widgets.RadioSelect
    )

    label = models.PositiveIntegerField(
        choices=[
            [1, 'It is fixed and does not change'],
            [2, 'The computer changes it in each round'],
            [3, 'I can change it in each round'],
        ],
        widget=widgets.RadioSelect
    )

    active = models.PositiveIntegerField(
        choices=[
            [1, 'When I propose a relation to another player regardless of he/she proposing a relation to me'],
            [2, 'When another player proposes a relation to me regardless of me proposing a relation to him/her'],
            [3, 'When I propose a relation to a player who also proposes a relation to me']
        ],
        widget=widgets.RadioSelect
    )

    count = models.PositiveIntegerField(
        choices=[
            [1, '5'],
            [2, '4'],
            [3, '3']
        ],
        widget=widgets.RadioSelect
    )

    pay_coord = models.PositiveIntegerField(
        choices=[
            [1, 'I gain 6 and pay the cost of 2 = 4 points in total'],
            [2, 'I gain 4 and pay the cost of 2 = 2 points in total'],
            [3, 'I gain 0 and pay the cost of 2 = -2 points in total']
        ],
        widget=widgets.RadioSelect
    )

    pay_nocoord = models.PositiveIntegerField(
        choices=[
            [1, 'I gain 6 and pay the cost of 2 = 4 points in total'],
            [2, 'I gain 4 and pay the cost of 2 = 2 points in total'],
            [3, 'I gain 0 and pay the cost of 2 = -2 points in total']
        ],
        widget=widgets.RadioSelect
    )
