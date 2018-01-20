#!/usr/bin/env python

import sys
import yaml

# check args
myself = sys.argv[0]
if len(sys.argv) != 2:
    print "error: invalid number of arguments."
    print "usage:\t" + myself + " [path to YAML file]"
    sys.exit(1)

infile = sys.argv[1]


with open(infile, 'r') as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)
