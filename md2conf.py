import sys, re
MAP1 = {
    'full name': 'FULL_NAME',
    'alias': 'OTHER_NAME',
    'version': 'VERSION',
    'description':  'DESCRIPTION',
    'authors': 'AUTHOR',
    'web/ftp': 'URL',
    'web':'URL',
    'source code language': 'LANGUAGE',
    'operating systems': 'OS',
    'executables': 'EXE',
    'reference': 'REFERENCE',
    'availability':'AVAILABILITY',
    'price':'AVAILABILITY',
    'vender':'AVAILABILITY'
    }
FIELDS = ['name', 'FULL_NAME', 'OTHER_NAME', 'VERSION', 'DESCRIPTION', 'AUTHOR', 'URL', 'LANGUAGE', 'OS', 'EXE', 'REFERENCE', 'RELATED', 'AVAILABILITY']

def dict2conf(d):
    d['name'] = d['name'].replace('(see', '(see also') if not 'see also' in d['name'] else d['name']
    d['name'] = re.sub(r'other name|other names', 'previously', d['name'])
    if 'previously' in d['name']:
        value = d['name'].split('(')
        d['name'] = value[0].strip()
        if 'OTHER_NAME' in d:
            d['OTHER_NAME'][0] += ', ' + re.sub(r'previously|previously:', '', value[1]).strip().strip(')')
        else:
            d['OTHER_NAME'] = [re.sub(r'previously|previously:', '', value[1]).strip().strip(')')]
    if 'see also' in d['name']:
        value = d['name'].split('(')
        d['name'] = value[0].strip()
        d['RELATED'] = [value[1].replace('see also', '').strip().strip(')')]
    if 'AUTHOR' in d:
        d['AUTHOR'][0] = d['AUTHOR'][0].replace(' and ', ', ')
        r = re.compile(r'(?:[^,(]|\([^)]*\))+')
        d['AUTHOR'] = [x.strip() for x in r.findall(d['AUTHOR'][0])]
    if 'URL' in d:
        d['URL'] = ';'.join(d['URL']).split(";")
    d['name'] = re.sub(r"\(|\)|,",'', d['name'])
    fname = d['name'].replace(' - ','-').replace('/', '&').replace(' ','_') + '.ini'
    with open(fname, 'w') as f:
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
        f.write('TAG=\n')
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
                print line
                try:
                    d[prev_key].append(line)
                except:
                    raise
