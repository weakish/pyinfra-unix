from pyinfra.api import deploy
from pyinfra.api.state import State
from pyinfra.api.host import Host
from pyinfra.modules import python
from unix.operation import pkcon
from unix.operation import freebsd

@deploy
def update(state: State, host: Host) -> None:
    if host.fact.os == 'Linux':
        if host.fact.linux_distribution["release_meta"]["ID"] == 'neon':
            pkcon.update(state, host)
        else:
            python.raise_exception(state, host, NotImplementedError)
    elif host.fact.os == 'FreeBSD':
        freebsd.update(state, host)
        freebsd.upgrade(state, host)
    else:
        python.raise_exception(state, host, NotImplementedError)