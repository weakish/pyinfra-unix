from typing import Generator, List, Dict, Union
from pyinfra.api import operation
from pyinfra.api.state import State
from pyinfra.api.host import Host


@operation
def update(state: State, host: Host) -> Generator[str, None, None]:
    """Download FreeBSD security patches."""
    yield "freebsd-update fetch --not-running-from-cron"


@operation
def upgrade(
    state: State, host: Host
) -> Generator[Dict[str, Union[str, List[int]]], None, None]:
    """Apply FreeBSD security patches."""
    command: Dict[str, Union[str, List[int]]] = {
        "command": "freebsd-update install",
        "success_exit_codes": [0, 2],  ## 2: no updates to install
    }
    yield command


@operation
def rollback(state: State, host: Host) -> Generator[str, None, None]:
    """Roll back the last set of changes."""
    yield "freebsd-update rollback"
