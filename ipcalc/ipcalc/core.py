"""core.py - SHARED. Tell the other person before changing anything here."""

FULL = 0xFFFFFFFF


def ip_to_int(ip: str) -> int:
    """'192.168.1.1' -> number. ValueError if bad."""
    parts = ip.strip().split(".")
    if len(parts) != 4:
        raise ValueError(f"'{ip}' must have 4 parts")
    n = 0
    for p in parts:
        if not p.isdigit() or not (0 <= int(p) <= 255):
            raise ValueError(f"'{p}' is not a valid number (0-255)")
        n = (n << 8) | int(p)
    return n


def int_to_ip(n: int) -> str:
    return ".".join(str((n >> s) & 0xFF) for s in (24, 16, 8, 0))


def prefix_to_mask(prefix: int) -> int:
    if not (0 <= prefix <= 32):
        raise ValueError("Prefix must be between 0 and 32")
    return (FULL << (32 - prefix)) & FULL


def mask_to_prefix(mask: int) -> int:
    inverted = ~mask & FULL
    if inverted & (inverted + 1):
        raise ValueError("Mask is not contiguous")
    return 32 - inverted.bit_length()


def parse_cidr(text: str):
    """'192.168.0.0/24' -> (address_int, prefix)"""
    if "/" not in text:
        raise ValueError("Use the form a.b.c.d/prefix")
    addr, pre = text.split("/", 1)
    if not pre.strip().isdigit():
        raise ValueError("Prefix must be a number")
    prefix = int(pre)
    prefix_to_mask(prefix)
    return ip_to_int(addr), prefix


# ---------------- TODO (agree on owner: suggested Wasay) ----------------
def make_subnet_row(name: str, network_int: int, prefix: int, requested: int) -> dict:
    """
    Build ONE row in the agreed row format (see README).
    Used by: f3 (each equal subnet) and f4 (each VLSM block).
    Decide together: what do /31 and /32 give for usable hosts?
    """
    raise NotImplementedError
