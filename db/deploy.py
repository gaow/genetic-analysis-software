#!/usr/bin/env python
from collections import OrderedDict
from argparse import ArgumentParser
import re, os, time, json
FIELDS = ['FULL_NAME', 'OTHER_NAME', 'VERSION', 'DESCRIPTION', 'YEAR', 'AUTHOR', 'URL', 'LANGUAGE', 'OS', 'EXE', 'REFERENCE', 'AVAILABILITY', 'RELATED']

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
    def __init__(self, files, id_file):
        self.data = SimpleCfgParser(files).data
        self.prefix = os.path.join(os.path.split(os.getcwd())[0], 'pages')
        self.id_file = id_file
        
    def MakePages(self):
        for name in self.data.keys():
            with open(os.path.join(self.prefix, self.data[name]['FileName'].replace('.ini', '.md')), 'w') as f:
                f.write('#{}\n'.format(name))
                for k in [x for x in FIELDS if x in self.data[name]] + [x for x in self.data[name] if x not in FIELDS]:
                    if k == 'FileName':
                        continue
                    f.write('##{}\n'.format(' '.join([x.capitalize() for x in k.split('_')]) if k not in ['URL', 'OS', 'EXE'] else k))
                    if len(self.data[name][k]) > 1:
                        for item in self.data[name][k]:
                            f.write('* {}\n'.format(item))
                    else:
                        item = self.data[name][k][0].replace('\\\\', '\n')
                        f.write('{}\n'.format(item))
                    f.write('\n')

    def MakeTocAlphabet(self):
        categories = []
        with open(os.path.join(self.prefix, 'toc.md'), 'w') as f:
            for name in self.data.keys():
                category = '0' if re.match(r"[-+]?\d+$", name[0]) is not None else name[0].upper()
                if category not in categories:
                    categories.append(category)
                    f.write('\n## {}\n'.format(category))
                desc_text = ', ' + self.data[name]['FULL_NAME'][0] if 'FULL_NAME' in self.data[name] else ''
                link = 'https://github.com/gaow/genetic-analysis-software/blob/master/pages/' + \
                  self.data[name]['FileName'].replace('.ini', '.md')
                f.write('* [{}]({}){}\n'.format(name, link, desc_text))

    def OpenComments(self):
        with open(self.id_file, 'r') as f:
            data = json.load(f)
        start = max(data.values()) + 1
        for name in self.data.keys():
            if name in data:
                continue
            else:
                # Open issue
                category = '0' if re.match(r"[-+]?\d+$", name[0]) is not None else name[0].upper()
                cmd = 'ghi open -L {0} -m "Comments on {1}"'.format(category, name)
                os.system(cmd)
                data[name] = start
                start += 1
                time.sleep(5)
        with open(self.id_file, 'w') as f:
            json.dump(data, f)
        # Update comment
        for name in self.data.keys():
            with open(os.path.join(self.prefix, self.data[name]['FileName'].replace('.ini', '.md')), 'a') as f:
                if name in data:
                    f.write('\n## [Reviews on {}](https://github.com/gaow/genetic-analysis-software/issues/{})'.\
                            format(name, data[name]))

def main(args):
    gp = GasParser(args.data, args.id)
    gp.MakePages()
    gp.MakeTocAlphabet()
    gp.OpenComments()

if __name__ == '__main__':
    parser = ArgumentParser(description = 'Utility to generate list of genetics software in various fashions',
                            epilog = '''2015 by Gao Wang''' )
    parser.add_argument('data', nargs = '+', help = 'Input files')
    parser.add_argument('--id', required = True, help = 'JSON file of program name and their assigned ID')
    main(parser.parse_args())
