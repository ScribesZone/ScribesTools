# coding=utf-8

import shutil

import tools

class Tool(tools.Tool):
    name = 'GanttProject'
    installPlatforms = ['*']
    bundles = {
        'ganttproject_zip' : {
            '*':  ['ganttproject-2.7-r1891.zip']
        }
    }
    locals=[
        'ganttproject.cmd',
    ]

    def doInstall(self):
        self.unzipResourceAndRenameToTarget(
            'ganttproject_zip', 'ganttproject-2.7-r1891')

    doCheck = tools.CmdsCheck(
        message = 'Next step should display ganttproject help',
        cmds = [ 'ganttproject.cmd -help' ],
    )

# FIXME: the tool reference must be automatically associated to the
# attribute via a metaclass
# TODO: implement the metaclass
Tool.doCheck.tool = Tool



