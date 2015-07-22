# coding=utf-8

NAME='GitHub'
PACKAGE='github'
BUNDLES={
    'Win':  'Git-1.9.5-preview20150319.exe',
}

import os
OS='Win'
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIR = os.path.dirname(THIS_DIR)
TARGET_DIR = os.path.join(os.environ['SCRIBETOOLS'],NAME)
FULL_BIN = os.path.join(SOURCE_DIR, 'downloads', 'Win', BUNDLES[OS])

def install():
    if not os.path.exists(TARGET_DIR): os.makedirs(TARGET_DIR)
    os.system(FULL_BIN)

def check():
    raw_input('Checking %s: next step should display git help ...'
              % NAME)
    os.system('git help')