"""
This type stub file was generated by pyright.
"""

from pyinfra.api import operation
from typing import Any, Optional

'''
The windows_files module handles windows filesystem state, file uploads and template generation.
'''
@operation(pipeline_facts={ 'windows_file': 'name' })
def file(state, host, name, present: bool = ..., assume_present: bool = ..., user: Optional[Any] = ..., group: Optional[Any] = ..., mode: Optional[Any] = ..., touch: bool = ..., create_remote_dir: bool = ...):
    '''
    Add/remove/update files.

    + name: name/path of the remote file
    + present: whether the file should exist
    + assume_present: whether to assume the file exists
    + TODO: user: user to own the files
    + TODO: group: group to own the files
    + TODO: mode: permissions of the files as an integer, eg: 755
    + touch: whether to touch the file
    + create_remote_dir: create the remote directory if it doesn't exist

    ``create_remote_dir``:
        If the remote directory does not exist it will be created using the same
        user & group as passed to ``files.put``. The mode will *not* be copied over,
        if this is required call ``files.directory`` separately.

    Example:

    .. code:: python

        files.file(
            {'Create c:\\temp\\hello.txt'},
            'c:\\temp\\hello.txt',
            touch=True,
        )
    '''
    ...

def windows_file(*args, **kwargs):
    ...

def _create_remote_dir(state, host, remote_filename, user, group):
    ...

@operation(pipeline_facts={ 'windows_directory': 'name' })
def directory(state, host, name, present: bool = ..., assume_present: bool = ..., user: Optional[Any] = ..., group: Optional[Any] = ..., mode: Optional[Any] = ..., recursive: bool = ...):
    '''
    Add/remove/update directories.

    + name: name/path of the remote folder
    + present: whether the folder should exist
    + assume_present: whether to assume the directory exists
    + TODO: user: user to own the folder
    + TODO: group: group to own the folder
    + TODO: mode: permissions of the folder
    + TODO: recursive: recursively apply user/group/mode

    Examples:

    .. code:: python

        files.directory(
            {'Ensure the c:\\temp\\dir_that_we_want_removed is removed'},
            'c:\\temp\\dir_that_we_want_removed',
            present=False,
        )

        files.directory(
            {'Ensure c:\\temp\\foo\\foo_dir exists'},
            'c:\\temp\\foo\\foo_dir',
            recursive=True,
        )

        # multiple directories
        dirs = ['c:\\temp\\foo_dir1', 'c:\\temp\\foo_dir2']
        for dir in dirs:
            files.directory(
                {'Ensure the directory `{}` exists'.format(dir)},
                dir,
            )

    '''
    ...

def windows_directory(*args, **kwargs):
    ...

