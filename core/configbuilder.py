'''
A module providing the ability to store data in a json file in a similar
fashion to a database

Made for antinub-gregbot project
'''
import os
import json
from collections import MutableMapping


class ConfigJSON(MutableMapping):
    '''
    Class for storing data in a json file
    '''
    def __init__(self, filename, readable=True):
        '''Initialize loading of underlying dict'''
        self.filename = filename
        if readable:
            self.indent = 4
            self.sort_keys = True
        else:
            self.indent = 0
            self.sort_keys = False
        self.store = dict()
        self.load()

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __str__(self):
        return str(self.store)

    def load(self):
        '''Load data from file'''
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as fileh:
                self.update(json.load(fileh))

    def dump(self):
        '''Write data to file'''
        with open(self.filename, 'w') as fileh:
            json.dump(self.store, fileh,
                      indent=self.indent, sort_keys=self.sort_keys)
