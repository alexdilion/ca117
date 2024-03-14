#!/usr/bin/env python3

import sys

sub_20_words = """zero one two three four five six seven eight nine ten 
                eleven twelve thirteen fourteen fifteen sixteen seventeen 
                eighteen nineteen""".split()
tens_words = "twenty thirty forty fifty sixty seventy eighty ninety".split()
                
def convertNumToWord(n):
    if n < 20:
        return sub_20_words[n]
    elif n < 100:
        if n % 10 == 0:
            return tens_words[n // 10 - 2]

        tens, ones = n // 10 - 2, n % 10
        return f"{tens_words[tens]}-{sub_20_words[ones]}"

    return "one hundred"

for line in sys.stdin:
    line = line.strip()
    print(" ".join([convertNumToWord(int(n)) for n in line.split()]))
