'''
A module providing the ability to store data in a yaml file in a similar
fashion to a database

Made for antinub-gregbot project
'''
import os
from collections import MutableMapping

import yaml


class ConfigYAML(MutableMapping):
    '''
    Class for storing data in a yaml file
    '''
    def __init__(self, filename, readable=True):
        '''Initialize loading of underlying dict'''
        self.filename = filename
        self.readable = readable
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
            with open(self.filename, 'r') as infile:
                self.update(yaml.load(infile))

    def dump(self):
        '''Write data to file'''
        with open(self.filename, 'w') as outfile:
            yaml.dump(self.store, outfile,
                      default_flow_style=not self.readable)
