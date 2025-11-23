#A washing machine allows you to wash a jacket, which takes 40 minutes,
#wash underwear, which takes 70 minutes, and wash shoes, which takes 20 minutes.
#In addition, it is possible to program an additional rinse (15 minutes) and an
#additional spin (9 minutes). The washing machine settings are saved in variables. 
#Write a program that calculates and prints the total washing time. Sample result:

#washing_product = "shoes"
#rinse = True
#spin = False
#Total washing time: 35 minutes

###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

if program == 'j':
    total_washing_time += 40
    print('washing_product = "jacket"')
elif program == 'u':
    total_washing_time += 70
    print('washing_product = "underwear"')
elif program == 's':
    total_washing_time += 20
    print('washing_product = "shoes"')

# 2. Sprawdzamy płukanie i dodajemy czas, jeśli trzeba
if extra_rinse == 'y':
    total_washing_time += 15
    print("rinse = True")
else:
    print("rinse = False")

# 3. Sprawdzamy wirowanie i dodajemy czas, jeśli trzeba
# Zauważ, że ten if jest niezależny od poprzedniego!
if extra_spin == 'y':
    total_washing_time += 9
    print("spin = True")
else:
    print("spin = False")

# 4. Wypisujemy wynik tylko raz na samym końcu
print(f'Total washing time: {total_washing_time} minutes')

