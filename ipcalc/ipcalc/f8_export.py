"""F8 - Plan export.  OWNER: Wasay"""


def export_txt(plan: dict, path: str) -> None:
    """Write the PLAN dict (from f3 or f4) as a readable text report. CALLED BY: gui"""
    raise NotImplementedError


def export_csv(plan: dict, path: str) -> None:
    """Write the PLAN dict as a CSV file. CALLED BY: gui"""
    raise NotImplementedError
