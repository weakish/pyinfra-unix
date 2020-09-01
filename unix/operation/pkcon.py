from typing import Generator, Optional
from pyinfra.api import operation, StringCommand
from pyinfra.api.host import Host
from pyinfra.api.state import State


@operation
def update(
    state: Optional[State] = None, host: Optional[Host] = None
) -> Generator[StringCommand, None, None]:  # noqa
    """Upgrade system via PackageKit console client."""
    yield StringCommand(
        "pkcon update --plain --noninteractive", success_exit_codes=[0, 5]
    )
