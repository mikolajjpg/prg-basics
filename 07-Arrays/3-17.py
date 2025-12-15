#Write a program that counts the number of occurrences of any value from a tuple. Sample result:
#Tuple: 50,20,40,50,30,50
#Value: 50
#Number of occurrences: 3
#Napisz program, który zlicza liczbę wystąpień dowolnej wartości z krotki. Przykładowy wynik:
my_tuple = (50,20,40,50,30,50)
value_to_find = 50
occurence_count = my_tuple.count(value_to_find)

print(f"Tuple: {str(my_tuple).strip('()')}") # strip usuwa nawiasy dla estetyki
print(f"Value: {value_to_find}")
print(f"Number of occurrences: {occurence_count}")


