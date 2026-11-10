"""F2 - Network information calculator.  OWNER: Saad"""
from .core import ip_to_int, int_to_ip, prefix_to_mask


def network_info(ip_int: int, prefix: int) -> dict:
    """
    Return: network, broadcast, wildcard, first host, last host,
    total addresses, usable hosts. Handle /31 and /32.
    CALLED BY: gui, (f3 and f4 may reuse the network/broadcast maths later)
    """
    raise NotImplementedError


def binary_view(ip_int: int, prefix: int) -> dict:
    """Address, mask, network in binary with the network/host boundary marked. CALLED BY: gui"""
    raise NotImplementedError
