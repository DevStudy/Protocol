from abstract_response import AbstractResponse
from data_types.tuple_table import TupleTable
from lobby.list_table_command import ListTableCommand

__author__ = 'ericmas001@gmail.com'



class ListTableResponse(AbstractResponse):
    def __init__(self, obj):
        super().__init__(obj, ListTableCommand(obj['Command']))
        self.tables = [TupleTable(x) for x in obj['Tables']]

    def __str__( self ):
        return '{0} => ({1})'.format(super().__str__(), ', '.join([x.__str__() for x in self.tables]))