# coding=utf-8

"""
Frontend for managing tools.

TODO: This framework is in construction
Eventually it should support something like

    python manage.py download GitHub
    python manage.py install GitHub
    python manage.py check GitHub
    # python manage.py copyFromLocalST XXX


"""
import importlib
import argparse

from tools import ROOT_SOURCE_DIR, SCRIBETOOLS, PLATFORM
import index


def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "commands",
        help="list of commands (install | check | download | extract)"
            "separated by commas",
        type=str)
    parser.add_argument(
        "packages",
        help="name(s) of the tool package(s) separated by commas"
             "(e.g. checkstyle,sqlite,schemaspy )",
        type=str)
    arguments = parser.parse_args()
    return arguments

def displayContext():
    print('TODO: THIS FRAMEWORK IS IN CONSTRUCTION')
    print('Resource directory    : %s' % ROOT_SOURCE_DIR)
    print('SRIBETOOLS directory  : %s' % SCRIBETOOLS)
    print('Platform              : %s' % PLATFORM)

def processCommand(command, toolPackage):
    try:
        tool_module = importlib.import_module(toolPackage)
    except ImportError:
        raise Exception('No tool named %s' % toolPackage)
    if command == 'download':
        tool_module.Tool().download()
    elif command == 'install':
        tool_module.Tool().install()
    elif command == 'check':
        tool_module.Tool().check()
    elif command == 'extract':
        tool_module.Tool().extract()
    else:
        raise Exception('command is invalid')

def processCommands(commands, toolPackages):
    for tool_package in toolPackages:
        for command in commands:
            processCommand(command, tool_package)

def getPackageList(packages):
    """ get a list a package name or groups and expand the groups """
    package_list = []
    for package in packages:
        if package in index.ALL.keys():
            print 'Group %s = %s' % (package,index.ALL[package])
            # this is a group. Expand it
            package_list.extend(index.ALL[package].split(','))
        else:
            # this is a reguar package
            package_list.append(package)
    print package_list
    return package_list

def main():
    args = parseArguments()
    command_list = args.commands.split(',')
    package_list = getPackageList(args.packages.split(','))
    processCommands(command_list, package_list)


if __name__ == "__main__":
    main()
