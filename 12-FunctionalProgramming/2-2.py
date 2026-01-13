names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

names1 = sorted(names, key=lambda x: len(x))
print(f'Unsorted list')
print("names = [")
for name in names:
    print(f" '{name}',")
print("]")
print()
print('Sorted list:')
print(*names1, sep='\n')