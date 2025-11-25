import amodule

x = input('Enter any text: ')
y = str(input('Enter letter to find in text: '))

number_of_letter = amodule.counter(x,y)

print(x)
print(f"The number of letter '{y}': {number_of_letter}")