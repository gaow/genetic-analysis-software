import sys, re
MAP1 = {
    'full name': 'FULL NAME',
    'version': 'VERSION',
    'description':  'DESCRIPTION',
    'authors': 'AUTHOR',
    'web/ftp': 'URL',
    'web':'URL',
    'source code language': 'LANGUAGE',
    'operating systems': 'OS',
    'executables': 'EXE',
    'reference': 'REFERENCE'
    }
FIELDS = ['name', 'FULL NAME', 'VERSION', 'DESCRIPTION', 'AUTHOR', 'URL', 'LANGUAGE', 'OS', 'EXE', 'REFERENCE']

def dict2conf(d):
    d['Tag'] = []
    d['Related'] = []
    d['name'] = d['name'].replace('(see', '(see also') if not 'see also' in d['name'] else d['name']
    if 'see also' in d['name']:
        value = d['name'].split('(')
        d['name'] = value[0].strip()
        d['Related'].append(value[1].replace('see also', '').strip().strip(')'))
    if 'AUTHOR' in d:
        d['AUTHOR'][0] = d['AUTHOR'][0].replace(' and ', ', ')
        r = re.compile(r'(?:[^,(]|\([^)]*\))+')
        d['AUTHOR'] = [x.strip() for x in r.findall(d['AUTHOR'][0])]
    with open(d['name'].replace('/', '&').replace(' ','_') + '.conf', 'w') as f:
        for key in FIELDS:
            try:
                if key == 'name':
                    f.write('[{}]\n'.format(d['name']))
                else:
                    for item in d[key]:
                        if item:
                            f.write('{}={}\n'.format(key, item))
            except KeyError:
                pass
    return {}

d = {}
prev_key = ''
for line in open('gas-html.md').readlines():
    if line.startswith('*'):
        if 'name' in d:
            d = dict2conf(d)
            prev_key = ''
        d['name'] = line[1:].strip()
    else:
        line = line.lstrip().lstrip('*').strip()
        if line:
            value = [x.strip() for x in line.split(':', 1)]
            if value[0].lower() in MAP1:
                d[MAP1[value[0].lower()]] = [value[1]]
                prev_key = MAP1[value[0].lower()]
            else:
                try:
                    d[prev_key].append(line)
                except:
                    print line
                    sys.exit()
