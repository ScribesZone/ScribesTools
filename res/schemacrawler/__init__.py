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
        self.unzipResourceAndRenameToTarget(
            'schemacrawler_zip', 'schemacrawler-12.06.03-main')

    doCheck = tools.CmdsCheck(
        message = 'Next step should display schemacrawler help',
        cmds = [ 'schemacrawler -version' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



