# coding=utf-8

import tools

class Tool(tools.Tool):
    name = 'Pandoc'
    bundles = {
        'exec' : {
            'Win':  ['Win','pandoc-1.15-windows.msi']
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
        cmd = (
            'msiexec /i %s APPLICATIONFOLDER=%s  ALLUSERS=1'
            % (bin, self.targetDir) )
        tools.command(cmd)

    doCheck = tools.CmdsCheck(
        message = 'Next step should display pandoc version',
        cmds = [ 'pandoc -v' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



