# IP Calculator for Subnet Design (CS3001, Group 5)

## Who owns what
| File                         | Feature                  | Owner  |
|------------------------------|--------------------------|--------|
| ipcalc/core.py               | shared helpers + row fmt | shared |
| ipcalc/f1_validation.py      | F1                       | Saad   |
| ipcalc/f2_network_info.py    | F2                       | Saad   |
| ipcalc/f3_fixed_subnetting.py| F3                       | Saad   |
| ipcalc/f6_overlap.py         | F6                       | Saad   |
| ipcalc/f4_vlsm.py            | F4                       | Wasay  |
| ipcalc/f5_summarization.py   | F5                       | Wasay  |
| ipcalc/f7_ipv6.py            | F7                       | Wasay  |
| ipcalc/f8_export.py          | F8                       | Wasay  |
| gui.py                       | Tkinter window           | both   |

## Who calls whom (arrows = "imports from")
- Every f*.py  -> core.py
- f3, f4       -> core.make_subnet_row   (same row format)
- f4           -> f1.parse_address_input (parent network input, later)
- f6           -> core helpers only
- f8           -> reads the "plan" dict made by f3 or f4
- gui.py       -> every f*.py

## Rules (keep these)
1. Only edit your own files. Need a change in core.py? Message the other person first.
2. Logic functions RETURN data. They never print() or input().
3. Bad input -> raise ValueError("clear message"). The GUI shows it.
4. Every function that makes a subnet table returns the PLAN format below.
5. Pull before you start. Push small and often. Never push code that crashes on import.

## Row format (one subnet)
{"name", "requested", "network", "prefix", "mask",
 "first", "last", "broadcast", "usable", "unused"}

## Plan format (F3 and F4 both return this, F6 and F8 read it)
{"parent": "192.168.0.0/24", "subnets": [row, row, ...], "free": [("192.168.0.128", 25), ...]}
(F3 returns "free": [] )
