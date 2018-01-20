#!/usr/bin/env python

import sys
import yaml


def out (s):
    sys.stdout.write(s)

uniq = 1

def getID():
    global uniq
    n = str(uniq)
    uniq += 1
    return n
    
def asAttr(attr, val):
    return " [" + attr + "=\"" + val + "\"]"

def render(ast, name=None):
    if name is None:
        name = getID()
        
    lab = ""
    edges = []  # (from, to, attr)
    
    if type(ast) is dict:
        for key,val in ast.iteritems():
            
            if type(val) is dict:
                child = getID()
                edges.append((name, child, asAttr("label", key)))
                render(val, child)
                
            elif type(val) is list:
                last = None
                for i in val:
                    child = getID()
                    edges.append((name, child, asAttr("label", key)))
                    render(i, child)
                    if last is not None:
                        edges.append((last, child, asAttr("style", "dashed")))
                    last = child
                
            else:
                lab += (str(key) + ": " + str(val) + "\\n")
                
    else:
        lab += str(ast)
    
    # output vertex
    out(name + asAttr("label", lab) + ";\n")
    
    # output edges
    for (src, dest, attr) in edges:
        out(src + " -> " + dest + attr + ";\n")
    



######################
# "main"

# check args
myself = sys.argv[0]
if len(sys.argv) != 2:
    print "error: invalid number of arguments."
    print "usage:\t" + myself + " [path to YAML file]"
    sys.exit(1)

infile = sys.argv[1]

with open(infile, 'r') as stream:
    try:
        ast = yaml.load(stream)

        out ("digraph graphname {\n")
        
        render(ast)
        
        out ("}\n")
        
    except yaml.YAMLError as exc:
        print(exc)
        sys.exit(1)
