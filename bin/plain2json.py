import json
import sys

if len(sys.argv) != 2:
    print "Usage: " + sys.argv[0] + " <plaintext file>"
    exit(1)

with open(sys.argv[1], 'r') as plaintext:
    request_data = {}
    request_data['name'] = 'metrics'
    request_data['columns'] = [ 'name', 'value', 'retval' ]
    request_data['points'] = []
    for line in plaintext.readlines():
        request_data['points'].append(line.strip().split(' '))
    print json.dumps([ request_data ], indent=2)
