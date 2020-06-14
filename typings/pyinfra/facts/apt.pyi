"""
This type stub file was generated by pyright.
"""

from pyinfra.api import FactBase

def parse_apt_repo(name):
    ...

class AptSources(FactBase):
    '''
    Returns a list of installed apt sources:

    .. code:: python

        {
            'type': 'deb',
            'url': 'http://archive.ubuntu.org',
            'distribution': 'trusty',
            'components', ['main', 'multiverse']
        },
        ...
    '''
    command = ...
    default = ...
    def process(self, output):
        ...
    


