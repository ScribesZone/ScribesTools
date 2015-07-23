# coding=utf-8

import shutil

import tools

class Tool(tools.Tool):
    name = 'UseOCL'
    installPlatforms = ['*']
    bundles = {
        'use_zip' : {
            '*':  ['sqlite-shell-win32-x86-3081002.zip']
        },
        # TODO: add notpad++ bundle
    }

    def doInstall(self):
        raise NotImplementedError()
        self.unzipContentIn('use')

    doCheck = tools.CmdsCheck(
        message = 'Next step should display use help',
        cmds = [ 'use -v' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



