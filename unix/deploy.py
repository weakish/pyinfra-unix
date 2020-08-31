import socket
from os import environ
from ipaddress import ip_address, IPv4Address, IPv6Address
from pathlib import PosixPath
from pyinfra.api import deploy
from pyinfra.api.state import State
from pyinfra.api.host import Host
from pyinfra.modules import apk, apt, brew, dnf, files, python, server
from paramiko.config import SSHConfig
from unix.operation import pkcon
from unix.operation import freebsd
from typing import Union


@deploy
def update(state: State, host: Host) -> None:
    """update system"""
    if host.fact.os == "Linux":
        if host.fact.linux_distribution["release_meta"]["ID"] == "neon":
            pkcon.update(state, host)
        elif host.fact.linux_distribution["release_meta"]["ID"] in ["debian", "ubuntu"]:
            apt.update(state, host)
            apt.upgrade(state, host)
        elif host.fact.linux_distribution["release_meta"]["ID"] == "fedora":
            dnf.update(state, host)
        elif host.fact.linux_distribution["release_meta"]["ID"] == "alpine":
            apk.update(state, host)
            apk.upgrade(state, host)

        else:
            python.raise_exception(state, host, NotImplementedError)
    elif host.fact.os == "FreeBSD":
        freebsd.update(state, host)
        freebsd.upgrade(state, host)
    elif host.fact.os == "Darwin":
        brew.update(state, host)
        brew.upgrade(state, host)
    else:
        python.raise_exception(state, host, NotImplementedError)


@deploy
def ipv6(state: State, host: Host) -> None:
    """Test if ipv6 configured correctly."""
    server.shell(state, host, "ping6 -c1 ::1")


def _get_host_ip(
    host: str, ssh_config_path: str = "~/.ssh/config"
) -> Union[IPv4Address, IPv6Address]:
    """
    1. If host.name is a short alias,
       we assume there is a corresponding record in `~/.ssh/config`:
        1.1 If the corresponding `HOSTNAME` value is an IP address,
            return it as the result.
        1.2 If the corresponding `HOSTNAME` is a domain,
            return the IP of the domain,
            assuming the domain is accessible from the local machine.
    2. If host.name is a domain, return its IP,
       assuming the domain is accessible from the local machine.
    3. Else raise an ValueError.
    """
    posix_path: PosixPath = PosixPath(ssh_config_path)
    path_with_user_expanded: PosixPath = posix_path.expanduser()
    config: SSHConfig = SSHConfig.from_path(str(path_with_user_expanded))
    # If `host.name` does not exist in `~/.ssh/config`,
    # `config.lookup(host.name)['hostname']` returns `host.name` itself.
    hostname: str = config.lookup(host)["hostname"]
    ip: Union[IPv4Address, IPv6Address]
    try:
        ip = ip_address(hostname)
    except ValueError:
        return ip_address(socket.gethostbyname(hostname))
    else:
        return ip


@deploy
def brook(state: State, host: Host) -> None:
    """Install brook."""
    if host.fact.arch == "x86_64":
        files.download(
            state,
            host,
            "https://github.com/txthinking/brook/releases/download/v20200909/brook_linux_amd64",  # noqa: E950
            "/usr/local/bin/brook",
            mode=755,
            sha256sum="efc4dc925bcaff4d33450fbcd02351da8f971f5cea6b84501a3d2a6f94876adf",  # noqa: E950
        )
        server.shell(
            state,
            host,
            f"nohup brook server -l {_get_host_ip(host.name)}:{environ['BROOK_PORT']} -p {environ['BROOK_PASSWORD']} > /dev/null 2> /dev/null &",  # noqa: B950
            success_exit_codes=[0, 1],
        )
    else:
        python.raise_exception(state, host, NotImplementedError)


@deploy
def wireguard(state: State, host: Host) -> None:
    """Install wireguard."""
    if host.fact.os == "Linux":
        if host.fact.linux_distribution["release_meta"]["ID"] in ["debian", "ubuntu"]:
            apt.packages(state, host, "wireguard")
        else:
            python.raise_exception(state, host, NotImplementedError)
    else:
        python.raise_exception(state, host, NotImplementedError)

    files.template(
        state,
        host,
        "templates/wg0.conf.j2",
        "/etc/wireguard/wg0.conf",
        wg_private_key=environ["WG_PRIVATE_KEY"],
        wg_port=environ["WG_PORT"],
        wg_interface=environ["WG_INTERFACE"],
        wg_peer_1_public_key=environ["WG_PEER_1_PUBLIC_KEY"],
        wg_peer_2_public_key=environ["WG_PEER_2_PUBLIC_KEY"],
    )

    server.shell(
        state,
        host,
        [
            "sysctl -w net.ipv4.ip_forward=1",
            "sysctl -w net.ipv6.conf.all.forwarding=1",
            "wg-quick up wg0",
        ],
        success_exit_codes=[0, 1],
    )
