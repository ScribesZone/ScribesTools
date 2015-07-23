# coding=utf-8
import os
import tools

class Tool(tools.Tool):
    name = 'Java'
    bundles = {
        'exec' : {
            'Win':  ['Win','jdk-8u51-windows-x64.exe']
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
        for d in ['jre','jdk']:
            tools.ensure_dir(os.path.join(self.sourceDir, d))
        bin = self.resourcePath('exec', 'Win')
        tools.command(bin)

    doCheck = tools.CmdsCheck(
        message = 'next step should display Java version',
        cmds = [ 'java -version' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool
