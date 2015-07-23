"""
Framework for tool installation.
This framework aims to simplify the installation of tools in a multiple
platform way. That's why python scripts are used instead of .cmd on windows
and .sh on unix platforms.

The framework is under construction. See GitHub

"""

import os
import abc

ROOT_SOURCE_DIR = os.path.dirname(os.path.realpath(__file__))
SCRIBETOOLS = os.environ['SCRIBETOOLS']
PLATFORM = 'Win'  # FIXME: compute the PLATFORM

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def command(cmd, showCommand=True):
    if showCommand:
        print('Executing: %s '%cmd)
    os.system(cmd)


class Tool(object):
    """
    Representation of a tool.

    This class should be subclassed in each tool directory. For instance in
    the github package one will find the class github.Tool.

    Attributes must be set by sub classes as class attributes. Methods can
    be overloaded if necessary and replace by "callable" in a declarative style.
    """
    name = None
    package = None
    installPlatforms = None
    bundles = None

    # def __init__(self, name, package=None, bundles=None, platforms=('*',)):
    #     self.name = name
    #     if package is None:
    #         self.package = name.lower()
    #     else:
    #         self.package = package
    #     self.bundles = bundles
    #     self.platforms = platforms


    def canInstallOnPlatform(self, platform):
        return (
            '*' in self.installPlatforms
            or platform in self.installPlatforms
        )

    @property
    def package(self):
        return self.name.lower()

    @property
    def sourceDir(self):
        return os.path.join(ROOT_SOURCE_DIR, self.package)

    @property
    def downloadsDir(self):
        return os.path.join(self.sourceDir, 'downloads')

    @property
    def targetDir(self):
        return os.path.join(SCRIBETOOLS, self.name)

    def resourceName(self, name, platform='*'):
        return os.path.join(*self.bundles[name][platform])

    def resourcePath(self, name, platform='*', directory='downloads'):
        resourceName = self.resourceName(name, platform=platform)
        path = os.path.join(self.sourceDir, directory, resourceName)
        if os.path.exists(path):
            return path
        else:
            raise ValueError(
                'The "%s" resource cannot be found for the platform "%s": '
                ' invalid path: %s' % (name, platform, path)
            )

    #===========================================================================
    #  install
    #===========================================================================

    def install(self):
        print("")
        print('='*80)
        print('INSTALLING %s ...' % self.name)
        print('Creating directory %s' % self.targetDir )
        ensure_dir(self.targetDir)
        self.doInstall()
        print('='*80)
        print("")

    @abc.abstractmethod
    def doInstall(self):
        pass

    def _failInstallOnPlatform(self):
        """
        raise an exception. To be used by subclasses
        """
        raise NotImplementedError(
            'No installer available on %s' % PLATFORM
        )


    #===========================================================================
    #  check
    #===========================================================================

    def check(self):
        print("")
        print('\n'+'.'*80)
        print('CHECKING %s ...' % self.name)
        if hasattr(self,'doCheck'):
            do_check = getattr(self, 'doCheck')
            do_check()
        print('.'*80+'\n')
        print("")



#===============================================================================
#  doCheck  strategies
#===============================================================================

class DoCheck(object):
    """
    Callable class for creating the doCheck method in a declarative way.
    """

    tool = None
    """
    Reference to the tool that own this check. This parameter is important
    to get access to information such as the installation directory of the
    tool.
    """

    def __init__(self, message=None):
        self.message=message

    def __call__(self):
        print(self.message)
        raw_input('Type any key to continue ...')


class CmdsCheck(DoCheck):

    def __init__(self, message=None, cmds=()):
        super(CmdsCheck,self).__init__(message=message)
        self.cmds = cmds

    def __call__(self):
        super(CmdsCheck, self).__call__()
        for cmd in self.cmds:
            command(cmd)
