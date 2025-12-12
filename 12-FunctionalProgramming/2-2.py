names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

names1 = sorted(names, key=len)
print(*names1, end="")