"""F1 - IPv4 input validation and classification.  OWNER: Saad"""
from .core import ip_to_int, mask_to_prefix, prefix_to_mask


def parse_address_input(text: str):
    """
    Accept '192.168.10.37/26' OR '192.168.10.37 255.255.255.192'.
    Returns (ip_int, prefix). Raises ValueError for bad input / non-contiguous mask.
    CALLED BY: f2, f4 (parent input), gui
    """
    raise NotImplementedError


def classify_address(ip_int: int) -> str:
    """Return 'A', 'B', 'C', 'D' or 'E' from the first octet. CALLED BY: f2, gui"""
    raise NotImplementedError


def address_type(ip_int: int) -> str:
    """'private' (RFC 1918), 'loopback', 'link-local' or 'public'. CALLED BY: f2, gui"""
    raise NotImplementedError
