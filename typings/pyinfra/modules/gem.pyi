"""
This type stub file was generated by pyright.
"""

from pyinfra.api import operation
from typing import Any, Optional

'''
Manage Ruby gem packages. (see https://rubygems.org/ )
'''
@operation
def packages(state, host, packages: Optional[Any] = ..., present: bool = ..., latest: bool = ...):
    '''
    Add/remove/update gem packages.

    + packages: list of packages to ensure
    + present: whether the packages should be installed
    + latest: whether to upgrade packages without a specified version

    Versions:
        Package versions can be pinned like gem: ``<pkg>:<version>``.

    Example:

    .. code:: python

        # Note: Assumes that 'gem' is installed.
        gem.packages(
            {'Install rspec'},
            'rspec',
        )
    '''
    ...
