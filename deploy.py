#!/usr/bin/env python
from collections import OrderedDict
from ConfigParser import RawConfigParser
import argparse

class MultiOrderedDict(OrderedDict):
    def __setitem__(self, key, value):
        if isinstance(value, list) and key in self:
            self[key].extend(value)
        else:
            super(OrderedDict, self).__setitem__(key, value)

class GasParser:
    def __init__(self, files):
        slef.config = ConfigParser.RawConfigParser(dict_type=MultiOrderedDict)
        self.config.read(files)

    def print(self):
        print self.config

def main(args):
    gp = GasParser(args.data)
    gp.print()

if __name__ == '__main__':
    parser = ArgumentParser(description = 'Utility to generate list of genetics software in various fashions',
                            epilog = '''2015 by Gao Wang''' )
    parser.add_argument('data', nargs = '+', help = 'Input files')
    main(parser.parse_args())
