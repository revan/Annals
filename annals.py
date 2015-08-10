#!/usr/bin/python3
import json
import sys
import subprocess
import time
from template import template
import os
import datetime

def make_filename():
	return datetime.date.today().isoformat() + '.json'

if len(sys.argv) != 2:
	print("USAGE: %s [config.json]" % sys.argv[0])

with open(sys.argv[1]) as conf_fp:
	conf = json.load(conf_fp)

filename = make_filename()

# call API
subprocess.call(conf['command'] + ' > %s' % filename, shell=True)

# add to config
conf['entries'].append(filename)
with open(sys.argv[1], 'w') as conf_fp:
	json.dump(conf, conf_fp)

# TODO update symlink

# Update template
with open(conf['output'], 'w') as out_fp:
	out_fp.write(template.render(title=conf['title'], files=conf['entries']))
