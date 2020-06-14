"""
This type stub file was generated by pyright.
"""

from pyinfra.api.util import memoize
from typing import Any, Optional

@memoize
def show_warning():
    ...

def make_names_data(image: Optional[Any] = ...):
    ...

def connect(state, host, for_fact: Optional[Any] = ...):
    ...

def disconnect(state, host):
    ...

def run_shell_command(state, host, command, get_pty: bool = ..., timeout: Optional[Any] = ..., stdin: Optional[Any] = ..., success_exit_codes: Optional[Any] = ..., print_output: bool = ..., print_input: bool = ..., return_combined_output: bool = ..., **command_kwargs):
    ...

def put_file(state, host, filename_or_io, remote_filename, print_output: bool = ..., print_input: bool = ..., **kwargs):
    '''
    Upload a file/IO object to the target Docker container by copying it to a
    temporary location and then uploading it into the container using ``docker cp``.
    '''
    ...

def get_file(state, host, remote_filename, filename_or_io, print_output: bool = ..., print_input: bool = ..., **kwargs):
    '''
    Download a file from the target Docker container by copying it to a temporary
    location and then reading that into our final file/IO object.
    '''
    ...
