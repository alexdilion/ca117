#!/usr/bin/env python3

import sys

words = sys.stdin.read().strip().split("\n")
q_but_no_u = [w for w in words if "q" in w.lower().replace("qu", "")]
print(f"Words with q but no u: {q_but_no_u}")
