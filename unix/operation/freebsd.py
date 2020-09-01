from typing import Generator, Optional
from pyinfra.api import operation, StringCommand
from pyinfra.api.host import Host
from pyinfra.api.state import State


@operation
def update(
    state: Optional[State] = None, host: Optional[Host] = None  # noqa
) -> Generator[str, None, None]:  # noqa
    """Download FreeBSD security patches."""
    yield "freebsd-update fetch --not-running-from-cron"


@operation
def upgrade(
    state: Optional[State] = None, host: Optional[Host] = None  # noqa
) -> Generator[StringCommand, None, None]:
    """Apply FreeBSD security patches."""
    yield StringCommand("freebsd-update install", success_exit_codes=[0, 2])


@operation
def rollback(
    state: Optional[State] = None, host: Optional[Host] = None  # noqa
) -> Generator[str, None, None]:
    """Roll back the last set of changes."""
    yield "freebsd-update rollback"
