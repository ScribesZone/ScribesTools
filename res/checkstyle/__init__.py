# coding=utf-8

import shutil

import tools

class Tool(tools.Tool):
    name = 'CheckStyle'
    installPlatforms = ['*']
    bundles = {
        'checkstyle_jar' : {
            '*':  ['checkstyle-6.8.1-all.jar']
        }
    }
    locals=[
        'checkstyle.cmd',
        'checkstyle.sh',
    ]

    def doInstall(self):
        self.ensureTargetDir()
        self.copyResourceToTarget('checkstyle_jar','checkstyle-all.jar')

    doCheck = tools.CmdsCheck(
        message = 'Next step should open checkstyle version',
        cmds = [ 'checkstyle -v' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



