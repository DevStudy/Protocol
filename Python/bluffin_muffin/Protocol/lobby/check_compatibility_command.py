from Python.bluffin_muffin.protocol.abstract_lobby_command import AbstractLobbyCommand

__author__ = 'ericmas001@gmail.com'



class CheckCompatibilityCommand(AbstractLobbyCommand):
    def __init__(self, obj):
        super().__init__(obj)
        self.implemented_protocol_version = obj['ImplementedProtocolVersion']

    def __str__( self ):
        return '{0} ({1})'.format(
            super().__str__(),
            self.implemented_protocol_version
        )

    def _encode_specific(self, d):
        super()._encode_specific(d)
        d['ImplementedProtocolVersion'] = self.implemented_protocol_version