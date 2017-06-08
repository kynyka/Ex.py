import random
import sys

if len(sys.argv) > 1:
    rang = int(sys.argv[1])
else:
    rang = 100

number = random.randint(1, rang)
print "Master, you rolls {0} (1-100)".format(number, rang)
