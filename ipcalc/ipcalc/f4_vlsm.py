"""F4 - VLSM subnet design.  OWNER: Wasay"""
from .core import int_to_ip, prefix_to_mask, parse_cidr, make_subnet_row


def prefix_for_hosts(hosts: int) -> int:
    """Smallest block that fits hosts+2. 50 -> 26, 25 -> 27, 10 -> 28, 2 -> 30."""
    raise NotImplementedError


def range_to_blocks(start: int, end: int) -> list:
    """Split a free range into the fewest valid CIDR blocks. [(start_int, prefix), ...]"""
    raise NotImplementedError


def vlsm_design(parent: str, requirements: list) -> dict:
    """
    parent: '192.168.0.0/24'   requirements: [('Admin', 50), ('Lab', 25), ...]
    Returns the PLAN dict. Raises ValueError if it does not fit.
    CALLED BY: gui, f8, f6
    """
    raise NotImplementedError
