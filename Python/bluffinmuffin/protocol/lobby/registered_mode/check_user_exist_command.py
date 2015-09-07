from bluffinmuffin.protocol.interfaces import AbstractLobbyCommand


class CheckUserExistCommand(AbstractLobbyCommand):
    def __init__(self, username):
        super().__init__()
        self.username = username

    def __str__(self):
        return '{0} ({1})'.format(
            super().__str__(),
            self.username
        )

    def _encode_specific(self, d):
        super()._encode_specific(d)
        d['Username'] = self.username

    @classmethod
    def decode(cls, obj):
        return cls(
            obj['Username']
        )
