#!/usr/bin/env python3

import sys

def reducer():
    salesTotal = []
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split(",")

        thisKey, thisCost = data
        #timestamp, city, item, cost = data
        if oldKey is not None and oldKey != thisKey:
            print(oldKey + "," + str(max(salesTotal)))
            salesTotal = []

        oldKey = thisKey
        salesTotal.append(float(thisCost))

    if oldKey is not None:  # for the final key
        print(oldKey + "," + str(max(salesTotal)))

if __name__ == "__main__":
    # what function should run when python reducer.py is called?
    reducer()
