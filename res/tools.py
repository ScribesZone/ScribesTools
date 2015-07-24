"""
Framework for tool installation.
This framework aims to simplify the installation of tools in a multiple
platform way. That's why python scripts are used instead of .cmd on windows
and .sh on unix platforms.

The framework is under construction. See GitHub

"""

import os
import abc
import zipfile
import shutil

ROOT_SOURCE_DIR = os.path.dirname(os.path.realpath(__file__))
SCRIBETOOLS = os.environ['SCRIBETOOLS']
PLATFORM = 'Win'  # FIXME: compute the PLATFORM

def ensure_dir(path, show=True):
    if not os.path.exists(path):
        if show:
            print('**** Creating directory %s' % path)
        os.makedirs(path)
    else:
        if show:
            print('**** Directory %s already exists' % path)

def command(cmd, show=True):
    if show:
        print('**** Executing: %s '%cmd)
    os.system(cmd)

def unzip(zip, targetParent, show=True):
    if show:
        print('**** Unzip %s to %s' % (zip,targetParent)),
    # raw_input('continue')
    with zipfile.ZipFile(zip) as z:
        z.extractall(targetParent)
    if show:
        print(' done')

def unzipAndRenameDir(zip, targetParent, extractedDirName, newDirName,
                      show = True):
    """
    Unzip the given file in the target directory and then rename
    the resulting directory (extractedDirName) into a given name
    (newDirName). If the extracted directory or final directory exists
    then raises an exception.
    """
    extracted_dir = os.path.join(targetParent, extractedDirName)
    new_dir = os.path.join(targetParent, newDirName)
    if os.path.exists(extracted_dir):
        raise Exception('The directory %s already exist' % extracted_dir)
    if os.path.exists(new_dir):
        raise Exception('The directory %s already exist' % new_dir)
    unzip(zip, targetParent)
    if not os.path.isdir(extracted_dir):
        raise Exception('No directory %s' % extracted_dir)
    if show:
        print (
            '     Rename extracted root %s to %s'
            % (extractedDirName, newDirName)
        )
        os.rename(extracted_dir, new_dir)

def copyFile(sourceFile, targetFile, show=True):
    if show:
        print ('**** Copy: %s to %s' % (sourceFile,targetFile))
    shutil.copyfile(sourceFile, targetFile)



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


    def canInstallOnPlatform(self, platform=PLATFORM):
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
    def localsDir(self):
        return os.path.join(self.sourceDir, 'locals')

    def localPath(self, name):
        return os.path.join(self.localsDir, name)

    @property
    def targetDir(self):
        return os.path.join(SCRIBETOOLS, self.name)

    @property
    def targetParentDir(self):
        return os.path.dirname(self.targetDir)

    def resourceName(self, name, platform=PLATFORM):
        # check for exact pattern matching first
        if platform in self.bundles[name]:
            resource = self.bundles[name][platform]
        # then check if there is a '*' entry
        elif '*' in self.bundles[name]:
            resource = self.bundles[name]['*']
        else:
            raise Exception(
                'resourceName: Cannot find resources %s for platform %s'
                % (name, platform)
            )
        return os.path.join(*resource)

    def resourcePath(self, name, platform=PLATFORM, directory='downloads'):
        resourceName = self.resourceName(name, platform=platform)
        path = os.path.join(self.sourceDir, directory, resourceName)
        if os.path.exists(path):
            return path
        else:
            raise ValueError(
                'resourcePath: The "%s" resource cannot be found for the '
                'platform "%s":  invalid path: %s'
                % (name, platform, path)
            )

    #===========================================================================
    #  download
    #===========================================================================

    def download(self):
        raise NotImplementedError('download operation is not implemented yet')

    #===========================================================================
    #  install
    #===========================================================================

    def install(self):
        print("")
        print('='*80)
        print('INSTALLING %s ...' % self.name)
        self.doInstall()
        self.doCopyAllLocalsToTarget()
        print('='*80)
        print("")

    @abc.abstractmethod
    def doInstall(self):
        pass

    def doCopyAllLocalsToTarget(self):
        if hasattr(self, "locals"):
            for local in self.locals:
                self.copyLocalToTarget(local)

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


    #===========================================================================
    #  extract
    #===========================================================================

    def extract(self):
        if hasattr(self, "locals"):
            answer = raw_input('Do you want to update %s ?' % self.localsDir)
            if answer == 'y':
                for local in self.locals:
                    self.copyReferenceToLocal(local)
            else:
                print('changed nothing')

    #===========================================================================
    #  utilities
    #===========================================================================

    def ensureTargetDir(self):
        ensure_dir(self.targetDir)

    def copyResourceToTarget(self, resourceTag,
                             targetName=None, platform=PLATFORM):
        source_file = self.resourcePath(resourceTag, platform=platform)
        if targetName is None:
            targetName = self.resourceName(resourceTag, platform=platform)
        target_file = os.path.join(self.targetDir, targetName)
        copyFile(source_file, target_file)

    def copyLocalToTarget(self, name):
        """ Copy a local file from /locals to the target directory """
        source_file = self.localPath(name)
        target_file = os.path.join(self.targetDir, name)
        copyFile(source_file, target_file)

    def copyReferenceToLocal(self, name):
        """ Copy a reference file to /locals """
        reference_file = os.path.join(self.targetDir, name)
        local_file = self.localPath(name)
        copyFile(reference_file, local_file)

    def unzipResourceToTargetParent(self, resourceTag, platform=PLATFORM ):
        zip_file = self.resourcePath(resourceTag, platform=platform)
        unzip(zip_file, self.targetParentDir)

    def unzipResourceToTarget(self, resourceTag, platform=PLATFORM ):
        zip_file = self.resourcePath(resourceTag, platform=platform)
        unzip(zip_file, self.targetDir)

    def unzipResourceAndRenameToTarget(self, resourceTag, extractedDirName,
                                       platform=PLATFORM):
        zip_file = self.resourcePath(resourceTag, platform=platform)
        unzipAndRenameDir(
            zip_file, self.targetParentDir, extractedDirName, self.name)

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
