import re
import sys
res = []
for line in sys.stdin:
        word = line
        if word:
            res.append([word])
