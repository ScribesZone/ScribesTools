# coding=utf-8

import shutil

import tools

class Tool(tools.Tool):
    name = 'SQLite'
    installPlatforms = ['Win']
    bundles = {
        'sqlite_shell_zip' : {
            'Win':
                ['Win', 'sqlite-shell-win32-x86-3081002.zip']
        },
        'sqlite_jdbc_jar' : {
            '*': ['sqlite-jdbc-3.8.10.1.jar']
        },
    }

    def doInstall(self):
        self.ensureTargetDir()
        self.unzipResourceToTarget('sqlite_shell_zip')
        self.copyResourceToTarget('sqlite_jdbc_jar','sqlite-jdbc.jar')

    doCheck = tools.CmdsCheck(
        message = 'Next step should display schemaspy version',
        cmds = [ 'sqlite3 -version' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



