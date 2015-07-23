# coding=utf-8

"""
GitHub tool representation.

TODO: this is the referenced class. Other installation procedure should be
migrated to this framework.
"""

import tools



class Tool(tools.Tool):
    name = 'GitHub'
    bundles = {
        'exec' : {
            'Win':  ['Win','Git-1.9.5-preview20150319.exe']
        }
    }
    installPlatforms = ['Win']

    def doInstall(self):
        if tools.PLATFORM is 'Win':
            self.doInstallWin()
        else:
            self._failInstallOnPlatform()

    def doInstallWin(self):
        self.ensureTargetDir()
        bin = self.resourcePath('exec', 'Win')
        tools.command(bin)

    doCheck = tools.CmdsCheck(
        message = 'Next step should display git help',
        cmds = [ 'git help' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool
