# coding=utf-8

import shutil

import tools

class Tool(tools.Tool):
    name = 'Modelio'
    installPlatforms = ['*']
    bundles = {
        'modelio_open_zip' : {
            'Win':  ['Win','modelio-open-201502191121-win32.win32.x86_64.zip']
        }
    }

    def doInstall(self):
        if tools.PLATFORM == 'Win':
            # FIXME: to be implemented
            raise NotImplementedError()
            self.ensureTargetDir()
            self.unzipResourceToTargetThenRename('modelio_open_zip')
        else:
            raise NotImplementedError()

    doCheck = tools.CmdsCheck(
        message = 'Next step should open modelio',
        cmds = [ 'modelio' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



