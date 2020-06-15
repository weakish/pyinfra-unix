"""
This type stub file was generated by pyright.
"""

from pyinfra.api import operation
from typing import Any, Optional, Callable, overload
from pyinfra.api.state import State
from pyinfra.api.host import Host
from pyinfra.api.operation import OperationMeta

'''
The files module handles filesystem state, file uploads and template generation.
'''

# Until Pyright fix #728, I have to modify all @operation functions with pipeline_facts:
# https://github.com/microsoft/pyright/issues/728

def download(state: State, host: Host,
    source_url: str, destination: str,
    user: Optional[str] = None,
    group: Optional[str] = None,
    mode: Optional[int] = None,
    cache_time: Optional[int] = None,
    force: bool = False,
    sha256sum: Optional[str] = None,
    sha1sum: Optional[str] = None,
    md5sum: Optional[str] = None) -> OperationMeta:
    '''
    Download files from remote locations using curl or wget.

    + source_url: source URL of the file
    + destination: where to save the file
    + user: user to own the files
    + group: group to own the files
    + mode: permissions of the files
    + cache_time: if the file exists already, re-download after this time (in seconds)
    + force: always download the file, even if it already exists
    + sha256sum: sha256 hash to checksum the downloaded file against
    + sha1sum: sha1 hash to checksum the downloaded file against
    + md5sum: md5 hash to checksum the downloaded file against
    '''
    ...

@operation
def line(state, host, name, line, present: bool = ..., replace: Optional[Any] = ..., flags: Optional[Any] = ...):
    '''
    Ensure lines in files using grep to locate and sed to replace.

    + name: target remote file to edit
    + line: string or regex matching the target line
    + present: whether the line should be in the file
    + replace: text to replace entire matching lines when ``present=True``
    + flags: list of flags to pass to sed when replacing/deleting

    Regex line matching:
        Unless line matches a line (starts with ^, ends $), pyinfra will wrap it such that
        it does, like: ``^.*LINE.*$``. This means we don't swap parts of lines out. To
        change bits of lines, see ``files.replace``.

    Regex line escaping:
        If matching special characters (eg a crontab line containing *), remember to escape
        it first using Python's ``re.escape``.

    Examples:

    .. code:: python

        # prepare to do some maintenance
        maintenance_line = 'SYSTEM IS DOWN FOR MAINTENANCE'
        files.line(
            {'Add the down-for-maintence line in /etc/motd'},
            '/etc/motd',
            maintenance_line,
        )

        # Then, after the mantenance is done, remove the maintenance line
        files.line(
            {'Remove the down-for-maintenance line in /etc/motd'},
            '/etc/motd',
            maintenance_line,
            replace='',
            present=False,
        )

        # example where there is '*' in the line
        files.line(
            {'Ensure /netboot/nfs is in /etc/exports'},
            '/etc/exports',
            r'/netboot/nfs .*',
            replace='/netboot/nfs *(ro,sync,no_wdelay,insecure_locks,no_root_squash,'
            'insecure,no_subtree_check)',
        )

        files.line(
            {'Ensure myweb can run /usr/bin/python3 without password'},
            '/etc/sudoers',
            r'myweb .*',
            replace='myweb ALL=(ALL) NOPASSWD: /usr/bin/python3',
        )

        # example when there are double quotes (")
        line = 'QUOTAUSER=""'
        results = files.line(
            {'Example with double quotes (")'},
            '/etc/adduser.conf',
            '^{}$'.format(line),
            replace=line,
        )
        print(results.changed)

    '''
    ...

@operation
def replace(state, host, name, match, replace, flags: Optional[Any] = ...):
    '''
    A simple shortcut for replacing text in files with sed.

    + name: target remote file to edit
    + match: text/regex to match for
    + replace: text to replace with
    + flags: list of flags to pass to sed

    Example:

    .. code:: python

        files.replace(
            {'Change part of a line in a file'},
            '/etc/motd',
            'verboten',
            'forbidden',
        )
    '''
    ...

@operation(pipeline_facts={ 'find_files': 'destination' })
def sync(state, host, source, destination, user: Optional[Any] = ..., group: Optional[Any] = ..., mode: Optional[Any] = ..., delete: bool = ..., exclude: Optional[Any] = ..., exclude_dir: Optional[Any] = ..., add_deploy_dir: bool = ...):
    '''
    Syncs a local directory with a remote one, with delete support. Note that delete will
    remove extra files on the remote side, but not extra directories.

    + source: local directory to sync
    + destination: remote directory to sync to
    + user: user to own the files and directories
    + group: group to own the files and directories
    + mode: permissions of the files
    + delete: delete remote files not present locally
    + exclude: string or list/tuple of strings to match & exclude files (eg *.pyc)
    + exclude_dir: string or list/tuple of strings to match & exclude directories (eg node_modules)

    Example:

    .. code:: python

        # Sync local files/tempdir to remote /tmp/tempdir
        files.sync(
            {'Sync a local directory with remote'},
            'files/tempdir',
            '/tmp/tempdir',
        )
    '''
    ...

def _create_remote_dir(state, host, remote_filename, user, group):
    ...

@operation(pipeline_facts={ 'file': 'remote_filename','sha1_file': 'remote_filename' })
def get(state, host, remote_filename, local_filename, add_deploy_dir: bool = ..., create_local_dir: bool = ..., force: bool = ...):
    '''
    Download a file from the remote system.

    + remote_filename: the remote filename to download
    + local_filename: the local filename to download the file to
    + add_deploy_dir: local_filename is relative to the deploy directory
    + create_local_dir: create the local directory if it doesn't exist
    + force: always download the file, even if the local copy matches

    Note:
        This operation is not suitable for large files as it may involve copying
        the remote file before downloading it.

    Example:

    .. code:: python

        files.get(
            {'Download a file from a remote'},
            '/etc/centos-release',
            '/tmp/whocares',
        )

    '''
    ...

@operation(pipeline_facts={ 'file': 'remote_filename','sha1_file': 'remote_filename' })
def put(state, host, local_filename, remote_filename, user: Optional[Any] = ..., group: Optional[Any] = ..., mode: Optional[Any] = ..., add_deploy_dir: bool = ..., create_remote_dir: bool = ..., force: bool = ..., assume_exists: bool = ...):
    '''
    Upload a local file to the remote system.

    + local_filename: local filename
    + remote_filename: remote filename
    + user: user to own the files
    + group: group to own the files
    + mode: permissions of the files
    + add_deploy_dir: local_filename is relative to the deploy directory
    + create_remote_dir: create the remote directory if it doesn't exist
    + force: always upload the file, even if the remote copy matches
    + assume_exists: whether to assume the local file exists

    ``create_remote_dir``:
        If the remote directory does not exist it will be created using the same
        user & group as passed to ``files.put``. The mode will *not* be copied over,
        if this is required call ``files.directory`` separately.

    Note:
        This operation is not suitable for large files as it may involve copying
        the file before uploading it.

    Examples:

    .. code:: python

        # Note: This requires a 'files/motd' file on the local filesystem
        files.put(
            {'Update the message of the day file'},
            'files/motd',
            '/etc/motd',
            mode='644',
        )

    '''
    ...

@operation
def template(state, host, template_filename, remote_filename, user: Optional[Any] = ..., group: Optional[Any] = ..., mode: Optional[Any] = ..., create_remote_dir: bool = ..., **data):
    '''
    Generate a template using jinja2 and write it to the remote system.

    + template_filename: local template filename
    + remote_filename: remote filename
    + user: user to own the files
    + group: group to own the files
    + mode: permissions of the files
    + create_remote_dir: create the remote directory if it doesn't exist

    ``create_remote_dir``:
        If the remote directory does not exist it will be created using the same
        user & group as passed to ``files.put``. The mode will *not* be copied over,
        if this is required call ``files.directory`` separately.

    Notes:
       Common convention is to store templates in a "templates" directory and
       have a filename suffix with '.j2' (for jinja2).

       For information on the template syntax, see
       `the jinja2 docs <https://jinja.palletsprojects.com>`_.

    Examples:

    .. code:: python

        files.template(
            {'Create a templated file'},
            'templates/somefile.conf.j2',
            '/etc/somefile.conf',
        )

        files.template(
            {'Create service file'},
            'templates/myweb.service.j2',
            '/etc/systemd/system/myweb.service',
            mode='755',
            user='root',
            group='root',
        )

        # Example showing how to pass python variable to template file.
        # The .j2 file can use `{{ foo_variable }}` to be interpolated.
        foo_variable = 'This is some foo variable contents'
        files.template(
            {'Create a templated file'},
            'templates/foo.j2',
            '/tmp/foo',
            foo_variable=foo_variable,
        )

    '''
    ...

@operation(pipeline_facts={ 'link': 'name' })
def link(state, host, name, target: Optional[Any] = ..., present: bool = ..., assume_present: bool = ..., user: Optional[Any] = ..., group: Optional[Any] = ..., symbolic: bool = ..., create_remote_dir: bool = ...):
    '''
    Add/remove/update links.

    + name: the name of the link
    + target: the file/directory the link points to
    + present: whether the link should exist
    + assume_present: whether to assume the link exists
    + user: user to own the link
    + group: group to own the link
    + symbolic: whether to make a symbolic link (vs hard link)
    + create_remote_dir: create the remote directory if it doesn't exist

    ``create_remote_dir``:
        If the remote directory does not exist it will be created using the same
        user & group as passed to ``files.put``. The mode will *not* be copied over,
        if this is required call ``files.directory`` separately.

    Source changes:
        If the link exists and points to a different target, pyinfra will remove it and
        recreate a new one pointing to then new target.

    Examples:

    .. code:: python

        # simple example showing how to link to a file
        files.link(
            {'Create link /etc/issue2 that points to /etc/issue'},
            '/etc/issue2',
            '/etc/issue',
        )


        # complex example demonstrating the assume_present option
        from pyinfra.modules import apt, files

        install_nginx = apt.packages(
            {'Install nginx'},
            'nginx',
        )

        files.link(
            {'Remove default nginx site'},
            '/etc/nginx/sites-enabled/default',
            present=False,
            assume_present=install_nginx.changed,
        )

    '''
    ...

@operation(pipeline_facts={ 'file': 'name' })
def file(state, host, name, present: bool = ..., assume_present: bool = ..., user: Optional[Any] = ..., group: Optional[Any] = ..., mode: Optional[Any] = ..., touch: bool = ..., create_remote_dir: bool = ...):
    '''
    Add/remove/update files.

    + name: name/path of the remote file
    + present: whether the file should exist
    + assume_present: whether to assume the file exists
    + user: user to own the files
    + group: group to own the files
    + mode: permissions of the files as an integer, eg: 755
    + touch: whether to touch the file
    + create_remote_dir: create the remote directory if it doesn't exist

    ``create_remote_dir``:
        If the remote directory does not exist it will be created using the same
        user & group as passed to ``files.put``. The mode will *not* be copied over,
        if this is required call ``files.directory`` separately.

    Example:

    .. code:: python

        # Note: The directory /tmp/secret will get created with the default umask.
        files.file(
            {'Create /tmp/secret/file'},
            '/tmp/secret/file',
            mode='600',
            user='root',
            group='root',
            touch=True,
            create_remote_dir=True,
        )
    '''
    ...

@operation(pipeline_facts={ 'directory': 'name' })
def directory(state, host, name, present: bool = ..., assume_present: bool = ..., user: Optional[Any] = ..., group: Optional[Any] = ..., mode: Optional[Any] = ..., recursive: bool = ...):
    '''
    Add/remove/update directories.

    + name: name/path of the remote folder
    + present: whether the folder should exist
    + assume_present: whether to assume the directory exists
    + user: user to own the folder
    + group: group to own the folder
    + mode: permissions of the folder
    + recursive: recursively apply user/group/mode

    Examples:

    .. code:: python

        files.directory(
            {'Ensure the /tmp/dir_that_we_want_removed is removed'},
            '/tmp/dir_that_we_want_removed',
            present=False,
        )

        files.directory(
            {'Ensure /web exists'},
            '/web',
            user='myweb',
            group='myweb',
        )

        # multiple directories
        dirs = ['/netboot/tftp', '/netboot/nfs']
        for dir in dirs:
            files.directory(
                {'Ensure the directory `{}` exists'.format(dir)},
                dir,
            )

    '''
    ...

