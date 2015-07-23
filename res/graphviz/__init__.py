# coding=utf-8

import tools



class Tool(tools.Tool):
    name = 'Graphviz'
    bundles = {
        'exec' : {
            'Win':  ['Win','graphviz-2.38.msi']
        }
    }
    installPlatforms = ['Win']

    def doInstall(self):
        if tools.PLATFORM is 'Win':
            self.doInstallWin()
        else:
            self._failInstallOnPlatform()

    def doInstallWin(self):
        bin = self.resourcePath('exec', 'Win')
        cmd = 'msiexec /i %s TARGETDIR=%s  ALLUSER=1' % (bin, self.targetDir)
        tools.command(cmd)

    doCheck = tools.CmdsCheck(
        message = 'Next step should display graphviz/dot version',
        cmds = [ 'dot -V' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



