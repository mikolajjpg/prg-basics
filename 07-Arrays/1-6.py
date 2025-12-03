#Napisz program, który wypisuje nazwę dnia tygodnia dla podanego numeru dnia.
#Następnie, używając zdefiniowanej funkcji, 
#wypisuje nazwę dnia tygodnia dla następujących numerów dni: 1, 4, 7.

###
# Zwraca nazwę dnia tygodnia dla podanego numeru dnia (1-poniedziałek ... 7-niedziela)
#
def weekday(n):
    weekdays = ["Poniedziałek", "Wtorek", "Środa",
    "Czwartek", "Piątek", "Sobota", "Niedziela"]
    if n ==1:
        return weekdays[0]
    if n==2:
        return weekdays[1]
    if n==3:
        return weekdays[2]
    if n==4:
        return weekdays[3]
    if n==5:
        return weekdays[4]
    if n==6:
        return weekdays[5]
    if n==7:
        return weekdays[6]
    
if __name__ == "__main__":
    print( weekday(7) )