"""F3 - Fixed-length subnetting.  OWNER: Saad"""
from .core import make_subnet_row


def split_into_n(parent: str, n: int) -> dict:
    """Split parent into N equal subnets. Returns the PLAN dict. CALLED BY: gui, f8, f6"""
    raise NotImplementedError


def split_by_hosts(parent: str, hosts: int) -> dict:
    """Subnets that each hold at least H hosts. Returns the PLAN dict. CALLED BY: gui, f8, f6"""
    raise NotImplementedError
