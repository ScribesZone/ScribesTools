# coding=utf-8

import shutil

import tools

class Tool(tools.Tool):
    name = 'UseOCL'
    installPlatforms = ['*']
    bundles = {
        'use_zip' : {
            '*':
                ['use-4.1.0.zip']
        },
        # TODO: add notpad++ bundle
    }

    def doInstall(self):
        self.unzipResourceAndRenameToTarget(
            'use_zip', 'use-4.1.0')

    doCheck = tools.CmdsCheck(
        message = 'Next step should display use help',
        cmds = [ 'use -V' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



