import re
from collections import Counter
c = Counter()

with open('optimus_prime.ged', 'r') as f:
    s = f.read()
    lst = re.findall('US[0-9]{2}_T[0-9]{2}_I[0-9]{2} INDI', s)
    for word in lst:
        c[word] += 1

print(c)