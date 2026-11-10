"""F5 - Route summarization (supernetting).  OWNER: Wasay"""
from .core import parse_cidr, int_to_ip, prefix_to_mask


def summarize(networks: list) -> dict:
    """
    networks: ['192.168.0.0/24', '192.168.1.0/24', ...]
    Returns {"summary": "192.168.0.0/23", "exact": True/False}.
    exact=False means the summary also covers extra addresses.
    CALLED BY: gui
    """
    raise NotImplementedError
