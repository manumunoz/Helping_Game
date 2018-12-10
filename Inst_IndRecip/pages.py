from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomeInst(Page):
    pass


class SummaryInstWP(WaitPage):
    pass


class SummaryInst(Page):
    pass

class PlayerAWP(WaitPage):
    pass

class PlayerA(Page):
    pass

class PlayerBWP(WaitPage):
    pass

class PlayerB(Page):
    pass

# You will observe your type, choose connection, observe the network, choose an action, and observe your earnings.


page_sequence = [
    WelcomeInst,
    SummaryInstWP,
    SummaryInst,
    PlayerAWP,
    PlayerA,
    PlayerBWP,
    PlayerB,
]
