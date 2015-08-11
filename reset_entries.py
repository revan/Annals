#!/usr/bin/python3
import json
import sys

if len(sys.argv) != 2:
	print('USAGE: %s [config.json]' % sys.argv[0])
	sys.exit(1)

with open(sys.argv[1]) as in_fp:
	conf = json.load(in_fp)

conf['entries'] = []

with open(sys.argv[1], 'w') as out_fp:
	json.dump(conf, out_fp)

print('Reset entries.')