# coding=utf-8

BIN='Win\graphviz-2.38.msi'
PACKAGE_NAME='Graphviz'

NAME='GraphViz'
PACKAGE='graphviz'
BUNDLES={
    'Win':  'Git-1.9.5-preview20150319.exe',
}

import os
OS='Win'

import os
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIR = os.path.dirname(THIS_DIR)
TARGET_DIR = os.path.join(os.environ['SCRIBETOOLS'],'Git')
FULL_BIN = os.path.join(SOURCE_DIR, 'downloads', BIN)

def install():
    if not os.path.exists(TARGET_DIR): os.makedirs(TARGET_DIR)
    os.system('msiexec /i %s TARGETDIR=%s  ALLUSER=1' % (FULL_BIN,TARGET_DIR))

def check():
    raw_input('Checking: next step should display graphviz/dot version ...')
    os.system('dot -V')

