#The following array represents a square matrix and contains values:
#[
   #[0,0,0],
   #[0,0,0],
   #[0,0,0]
#]
#Create a program that replaces the values of the main diagonal with 1. Use a loop statement.
 #Print the modified array. Sample result:

#1 0 0
#0 1 0
#0 0 1

arr = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
for i in range(len(arr)): # lub range(3)
    arr[i][i] = 1

# 2. WYŚWIETLANIE
# Tutaj licznik nie jest konieczny, bo masz listę list.
# Koniec wewnętrznej pętli oznacza koniec wiersza.

licznik = 0
for number in arr:
    for item in number:
           print(item, end=" ")

           licznik += 1

           if licznik ==3:
                 print()
                 licznik =0
            