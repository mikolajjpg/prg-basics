#Tablica zawiera wartości: 15, 8, 31, 47, 2, 19.
#Utwórz program, który oblicza i wyświetla tablicę oraz średnią arytmetyczną wartości tablicowych.
#Użyj instrukcji pętli „for”.

arr = [15, 8, 31, 47, 2, 19]
summary_of_arr= 0
for number in arr:
    summary_of_arr += number

print(summary_of_arr)
print(arr)

summary2 = 0
for number in arr:
    summary2 += number

ar_mean = summary2 / len(arr)

print(f'{ar_mean:.2f}')

