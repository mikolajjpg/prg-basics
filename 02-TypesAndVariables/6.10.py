#Every programming language has a number of ready-to-use functions that you can use to manipulate
#strings. The most commonly used ones in Python can be found at:
###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
x = movie.upper()
print(x)

# print title in small letters
y = movie.lower()
print(y)

# print how many times the vowel "e" appears in the title
z = movie.count("e")
print(z)

# print where in the text is the word "Lord"
u = movie.index("Lord")
print(u)

# print where in the text is the word "dragon"
v = movie.find("dragon")
print("none") if v == -1 else print(v)