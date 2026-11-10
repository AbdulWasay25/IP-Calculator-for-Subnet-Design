"""F7 - IPv6 prefix handling.  OWNER: Wasay
No dependency on core.py (IPv4 helpers). Uses its own 128-bit helpers."""


def expand_ipv6(text: str) -> str:
    """'2001:db8::1' -> full 8-group form. CALLED BY: gui"""
    raise NotImplementedError


def compress_ipv6(text: str) -> str:
    """Full form -> shortest form (RFC 5952). CALLED BY: gui"""
    raise NotImplementedError


def split_ipv6_prefix(prefix_text: str, new_prefix: int = 64, limit: int = 256) -> list:
    """'2001:db8:abcd::/48' -> list of /64 subnets. Use 'limit' so the GUI does not freeze. CALLED BY: gui"""
    raise NotImplementedError
