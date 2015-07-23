# coding=utf-8

import shutil

import tools

class Tool(tools.Tool):
    name = 'SQLite'
    installPlatforms = ['Win']
    bundles = {
        'sqlite_shell_zip' : {
            'Win':  ['sqlite-shell-win32-x86-3081002.zip']
        },
        'sqlite_jdbc_jar' : {
            '*': ['sqlite-jdbc-3.8.10.1.jar']
        },
    }

    def doInstall(self):
        self.ensureTargetDir()
        self.copyResourceToTarget('sqlite_jdbc_jar','sqlite-jdbc.jar')
        raise NotImplementedError()
        self.unzipContentIn()

    doCheck = tools.CmdsCheck(
        message = 'Next step should display schemaspy help',
        cmds = [ 'schemaspy' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



