# coding=utf-8

import shutil

import tools

class Tool(tools.Tool):
    name = 'SchemaSpy'
    installPlatforms = ['*']
    bundles = {
        'schemaspy_zip' : {
            '*':  ['schemaSpy_5.0.0.jar']
        }
    }
    locals=[
        'schemaspy.cmd',
        'schemaspy.sh',
        'sqlite.properties',
    ]

    def doInstall(self):
        self.ensureTargetDir()
        self.copyResourceToTarget('schemaspy_zip','schemaSpy_5.0.0.jar')

    doCheck = tools.CmdsCheck(
        message = 'Next step should display schemaspy help',
        cmds = [ 'schemaspy' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



