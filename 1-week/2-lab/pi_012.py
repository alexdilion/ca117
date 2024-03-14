#!/usr/bin/env python3

import sys
from math import pi

for decimal in sys.stdin:
    print(f"{pi:.{int(decimal)}f}")
