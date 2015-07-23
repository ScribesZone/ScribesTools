# coding=utf-8

"""
Frontend for managing tools.

TODO: This framework is in construction
Eventually it should support something like

    python manage.py download GitHub
    python manage.py install GitHub
    python manage.py check GitHub
    # python manage.py copyFromLocalST XXX


"""

from tools import ROOT_SOURCE_DIR, SCRIBETOOLS, PLATFORM

print('TODO: THIS FRAMEWORK IS IN CONSTRUCTION')
print('Resource directory    : %s' % ROOT_SOURCE_DIR)
print('SRIBETOOLS directory  : %s' % SCRIBETOOLS)
print('Platform              : %s' % PLATFORM)

#FIXME: this should be generalized.
#TODO: implement a small command line with "options" interface

import graphviz
graphviz.Tool().install()
graphviz.Tool().check()

import github
github.Tool().install()
github.Tool().check()
