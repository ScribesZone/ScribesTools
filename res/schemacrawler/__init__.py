# coding=utf-8

import shutil

import tools

class Tool(tools.Tool):
    name = 'SchemaCrawler'
    installPlatforms = ['*']
    bundles = {
        'schemacrawler_zip' : {
            '*':  ['schemacrawler-12.06.03-main.zip']
        }
    }
    locals=[
        'schemacrawler.cmd',
        'schemacrawler.sh',
    ]

    def doInstall(self):
        raise NotImplementedError()
        # FIXME: to be implemented
        self.unzipResourceToTargetThenRename('schemacrawler_zip')
        # TODO: Here we should modify the content of the properties file

    doCheck = tools.CmdsCheck(
        message = 'Next step should open ganttproject help',
        cmds = [ 'ganttproject.cmd -help' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



