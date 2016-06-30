#!/usr/bin/env python
"""
Testing tool 
"""

#import string
import sys
import time

if __name__ == "__main__":
    name = None
    age = 0
    try:
        name = sys.argv[1]
        age = str(sys.argv[2])
        msg = "Hello "+name+", you are "+str(age)
        time.sleep(180)
        if int(age) >40:
           sys.stderr.write('sorry, too old!')
           sys.exit(10)
        sys.stdout.write(msg)
    except:
        msg = "sorry, too old!"
        sys.stderr.write(msg)
        sys.exit(100)
