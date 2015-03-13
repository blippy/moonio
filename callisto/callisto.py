# http://ipython.org/ipython-doc/dev/api/generated/IPython.nbconvert.exporters.html.html#module-IPython.nbconvert.exporters.html

#print("again")
import os
#import fnmatch
import glob
from os import listdir
from os.path import isdir, isfile, getmtime

import IPython.nbconvert

def walk(root, result = []):
    for f in listdir(root):
        full = os.path.join(root, f)
        if isfile(full):
            if f.endswith(".ipynb"): result.append((root, f))
        if isdir(full):
            #print("hi", full)
            if f.endswith(".ipynb_checkpoints"): continue
            #print("scanning", full)
            walk(full)
    return result



def convert_one(src, dest):
    print("Converting", src, "to", dest)
    with open(src) as fp:
        nb = IPython.nbformat.reader.reads(fp.read())
    exporter = IPython.nbconvert.html.HTMLExporter()
    (body, resources) = exporter.from_notebook_node(nb)
    with open(dest, "w") as fh:
        fh.writelines(body)


def convert():
    '''Scan the current directory, converting files'''
    for d, f in walk('.'):
        full = d + "/" + f
        htm = full[:-5]+ "htm" # name of the htm file to be generated
        if os.path.exists(htm):
            if getmtime(full) >= getmtime(htm): convert_one(full, htm)
        else:
            convert_one(full, htm)

    
