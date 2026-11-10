"""F6 - Overlap and membership checking.  OWNER: Saad"""
from .core import ip_to_int, parse_cidr, prefix_to_mask


def ip_in_subnet(ip: str, subnet: str) -> bool:
    """Is this IP inside this 'a.b.c.d/p' subnet? CALLED BY: gui"""
    raise NotImplementedError


def find_overlaps(subnets: list) -> list:
    """Given ['a/p', 'b/p', ...] return the list of overlapping pairs. CALLED BY: gui, tests"""
    raise NotImplementedError


def verify_plan(plan: dict) -> list:
    """Run find_overlaps on a plan from f3 or f4. Empty list = good. CALLED BY: gui"""
    raise NotImplementedError
