from abstract_game_command import AbstractGameCommand

__author__ = 'ericmas001@gmail.com'



class PlayerJoinedCommand(AbstractGameCommand):
    def __init__(self, obj):
        super().__init__(obj)
        self.player_name = obj['PlayerName']

    def __str__( self ):
        return '{0} ({1})'.format(super().__str__(),self.player_name)
