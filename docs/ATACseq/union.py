import sys
import argparse
def union(x,y):
    filenames=x
    with open(y, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
union(sys.argv[1],sys.argv[2])
##needs a list