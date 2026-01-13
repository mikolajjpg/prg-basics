#The array below contains employee data:

#[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
#   ("Jackson","Peter"),("Johnson","Rick"),
 #  ("Lewis","Terry"),("Clarke","Robin")]
#Write a program that determines and displays a list of employees whose last names are given 
#in capital letters followed by first names, separated by commas. 
#Sample result:

#SMITH, Lucy
#JONES, Janet
#…
#…


employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

surname = list(map(lambda e : f"{e[0].upper()}, {e[1]}", employees))

for x in surname:
    print(x)