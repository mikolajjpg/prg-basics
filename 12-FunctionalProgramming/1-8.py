#Define an anonymous function initials(name,surname) that
#returns the first letters of the name and surname.

def main():
    
    initials = lambda name,surname : name[0] + surname[0]

    result = initials('Mikolaj','Ola')

    return result

if __name__=="__main__":
    print(main())