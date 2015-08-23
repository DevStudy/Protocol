from abstract_game_command import AbstractGameCommand

__author__ = 'ericmas001@gmail.com'



class GameStartedCommand(AbstractGameCommand):
    def __init__(self, obj):
        super().__init__(obj)
        self.needed_blind_amount = obj['NeededBlindAmount']

    def __str__( self ):
        return '{0} ({1})'.format(super().__str__(),self.needed_blind_amount)
