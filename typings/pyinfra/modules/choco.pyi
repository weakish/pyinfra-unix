"""
This type stub file was generated by pyright.
"""

from pyinfra.api import operation
from typing import Any, Optional

'''
Manage choco (Chocolatey) packages. (see https://chocolatey.org/ )
'''
@operation
def packages(state, host, packages: Optional[Any] = ..., present: bool = ..., latest: bool = ...):
    '''
    Add/remove/update choco packages.

    + packages: list of packages to ensure
    + present: whether the packages should be installed
    + latest: whether to upgrade packages without a specified version

    Versions:
        Package versions can be pinned like gem: ``<pkg>:<version>``.

    Example:

    .. code:: python

        # Note: Assumes that 'choco' is installed and
        #       user has Administrator permission.
        choco.packages(
            {'Install Notepad++'},
            'notepadplusplus',
        )
    '''
    ...

@operation
def install(state, host):
    '''
    Install choco (Chocolatey).
    '''
    ...
