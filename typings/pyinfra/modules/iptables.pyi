"""
This type stub file was generated by pyright.
"""

from pyinfra.api import operation
from typing import Any, Optional

'''
The iptables modules handles iptables rules
'''
@operation
def chain(state, host, name, present: bool = ..., table=..., policy: Optional[Any] = ..., version=...):
    '''
    Add/remove/update iptables chains.

    + name: the name of the chain
    + present: whether the chain should exist
    + table: the iptables table this chain should belong to
    + policy: the policy this table should have
    + version: whether to target iptables or ip6tables

    Policy:
        These can only be applied to system chains (FORWARD, INPUT, OUTPUT, etc).
    '''
    ...

@operation
def rule(state, host, chain, jump, present: bool = ..., table=..., append: bool = ..., version=..., protocol: Optional[Any] = ..., not_protocol: Optional[Any] = ..., source: Optional[Any] = ..., not_source: Optional[Any] = ..., destination: Optional[Any] = ..., not_destination: Optional[Any] = ..., in_interface: Optional[Any] = ..., not_in_interface: Optional[Any] = ..., out_interface: Optional[Any] = ..., not_out_interface: Optional[Any] = ..., to_destination: Optional[Any] = ..., to_source: Optional[Any] = ..., to_ports: Optional[Any] = ..., log_prefix: Optional[Any] = ..., destination_port: Optional[Any] = ..., source_port: Optional[Any] = ..., extras=...):
    '''
    Add/remove iptables rules.

    + chain: the chain this rule should live in
    + jump: the target of the rule
    + table: the iptables table this rule should belong to
    + append: whether to append or insert the rule (if not present)
    + version: whether to target iptables or ip6tables

    Iptables args:

    + protocol/not_protocol: filter by protocol (tcp or udp)
    + source/not_source: filter by source IPs
    + destination/not_destination: filter by destination IPs
    + in_interface/not_in_interface: filter by incoming interface
    + out_interface/not_out_interface: filter by outgoing interface
    + to_destination: where to route to when jump=DNAT
    + to_source: where to route to when jump=SNAT
    + to_ports: where to route to when jump=REDIRECT
    + log_prefix: prefix for the log of this rule when jump=LOG

    Extras:

    + extras: a place to define iptables extension arguments (eg --limit, --physdev)
    + destination_port: destination port (requires protocol)
    + source_port: source port (requires protocol)

    Examples:

    .. code:: python

        # Block SSH traffic

        iptables.rule(
            'INPUT', 'DROP',
            destination_port=22
        )


        # NAT traffic on from 8.8.8.8:53 to 8.8.4.4:8080

        iptables.rule(
            'PREROUTING', 'DNAT', table='nat',
            source='8.8.8.8', destination_port=53,
            to_destination='8.8.4.4:8080'
        )
    '''
    ...
