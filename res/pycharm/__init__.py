# coding=utf-8

import tools

class Tool(tools.Tool):
    name = 'PyCharm'
    bundles = {
        'exec_open' : {
            'Win':  ['Win','pycharm-community-4.5.3.exe']
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
        bin = self.resourcePath('exec_open', 'Win')
        tools.command(bin)

    doCheck = tools.CmdsCheck(
        message = 'Next step should open pycharm open',
        cmds = [ 'pycharm' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



