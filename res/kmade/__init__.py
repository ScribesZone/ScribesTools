# coding=utf-8

import shutil

import tools

class Tool(tools.Tool):
    name = 'KMADe'
    installPlatforms = ['*']
    bundles = {
        'kmade_zip' : {
            '*':  ['KMADe-1.2-dist.zip']
        }
    }
    locals=[
        'kmade.cmd',
        'kmade.sh',
    ]

    def doInstall(self):
        self.unzipResourceAndRenameToTarget(
            'kmade_zip', 'KMADe-1.2')

    doCheck = tools.CmdsCheck(
        message = 'Next step should open kmade',
        cmds = [ 'kmade' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



