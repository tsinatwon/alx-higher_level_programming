#!/usr/bin/python3
for p in range(10):
    for z in range(10):
        if p < z:
            if (p * 10 + z) != 89:
                print("{}{},".format(p, z), end=" ")
            else:
                print("{}{}".format(p, z))
