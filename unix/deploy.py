from pyinfra.api import deploy
from pyinfra.api.state import State
from pyinfra.api.host import Host
from pyinfra.modules import apk, apt, python, server
from unix.operation import pkcon
from unix.operation import freebsd


@deploy
def update(state: State, host: Host) -> None:
    """update system"""
    if host.fact.os == "Linux":
        if host.fact.linux_distribution["release_meta"]["ID"] == "neon":
            pkcon.update(state, host)
        elif host.fact.linux_distribution["release_meta"]["ID"] == "ubuntu":
            apt.update(state, host)
            apt.upgrade(state, host)
        elif host.fact.linux_distribution["release_meta"]["ID"] == "alpine":
            apk.update(state, host)
            apk.upgrade(state, host)
        else:
            python.raise_exception(state, host, NotImplementedError)
    elif host.fact.os == "FreeBSD":
        freebsd.update(state, host)
        freebsd.upgrade(state, host)
    else:
        python.raise_exception(state, host, NotImplementedError)


@deploy
def ipv6(state: State, host: Host) -> None:
    """Test if ipv6 configured correctly."""
    server.shell(state, host, "ping6 -c1 ::1")
