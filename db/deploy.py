#!/usr/bin/env python
from collections import OrderedDict
from argparse import ArgumentParser
import re, os
 
class SimpleCfgParser:
    def __init__(self, files):
        self.data = OrderedDict()
        for f in files:
            name, data = self.parse(f)
            self.data[name] = data

    def parse(self, f):
        data = OrderedDict()
        lines = [x.strip() for x in open(f).readlines()]
        name = re.sub(r'\[|\]', '', lines[0])
        for line in lines[1:]:
            k, v = line.split('=', 1)
            if not v:
                continue
            if k not in data:
                data[k] = [v]
            else:
                data[k].append(v)
        data['FileName'] = f
        return name, data

class GasParser:
    def __init__(self, files):
        self.data = SimpleCfgParser(files).data
        self.prefix = os.path.join(os.path.split(os.getcwd())[0], 'pages')
        
    def Print(self):
        for name in self.data.keys():
            with open(os.path.join(self.prefix, self.data[name]['FileName'].replace('.ini', '.md')), 'w') as f:
                del self.data[name]['FileName']
                f.write('#{}\n'.format(name))
                for k in self.data[name]:
                    f.write('##{}\n'.format(k.capitalize() if k not in ['URL', 'OS'] else k))
                    if len(self.data[name][k]) > 1:
                        for item in self.data[name][k]:
                            f.write('* {}\n'.format(item))
                    else:
                        item = self.data[name][k][0].replace('\\\\', '\n')
                        f.write('{}\n'.format(item))
                    f.write('\n')

def main(args):
    gp = GasParser(args.data)
    gp.Print()

if __name__ == '__main__':
    parser = ArgumentParser(description = 'Utility to generate list of genetics software in various fashions',
                            epilog = '''2015 by Gao Wang''' )
    parser.add_argument('data', nargs = '+', help = 'Input files')
    main(parser.parse_args())
