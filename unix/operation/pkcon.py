from typing import Generator, List, Dict, Union
from pyinfra.api import operation
from pyinfra.api.state import State
from pyinfra.api.host import Host


@operation
def update(
    state: State, host: Host
) -> Generator[Dict[str, Union[str, List[int]]], None, None]:
    """Upgrade system via PackageKit console client."""
    command: Dict[str, Union[str, List[int]]] = {
        "command": "pkcon update --plain --noninteractive",
        "success_exit_codes": [0, 5],  ## 5: no updates to install
    }
    yield command
