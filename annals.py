#!/usr/bin/python3
import json
import sys
import subprocess
import time
import os
import datetime

SYMLINK = 'latest'

def make_filename():
	return datetime.date.today().isoformat() + '.json'

if len(sys.argv) != 2:
	print("USAGE: %s [config.json]" % sys.argv[0])
	sys.exit(1)

with open(sys.argv[1]) as conf_fp:
	conf = json.load(conf_fp)

filename = make_filename()

# call API
subprocess.call(conf['command'] + ' > %s' % filename, shell=True)

# add to config
conf['entries'].append(filename)
with open(sys.argv[1], 'w') as conf_fp:
	json.dump(conf, conf_fp)

# update symlink
if os.path.exists(SYMLINK):
	os.unlink(SYMLINK)
os.symlink(filename, SYMLINK)

if 'index' in conf and conf['index']:
	# Update template
	from template import template
	with open('index.html', 'w') as out_fp:
		out_fp.write(template.render(title=conf['title'], files=conf['entries'], latest=SYMLINK))
