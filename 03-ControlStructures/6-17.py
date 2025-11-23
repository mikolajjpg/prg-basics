#Write a program that allows you to convert time in 24-hour format to 12-hour format.
#The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

#Enter time (24-hour format): 16:32
#Time in 12-hour format: 4:32pm

time = input('Enter time (24-hour format):')

hour_str = time[0:2]  # weźmie "16"
minute_str = time[3:] # weźmie "32"

# Krok 2: Zamiana godziny na liczbę
hour = int(hour_str)
suffix = "am" # Tu wpiszemy 'am' lub 'pm'

# Krok 3: Warunki (Twoje zadanie)
if hour == 0:
    # Co zrobić z północą?
   hour = 12 # pass to "nic nie rób", usuń to i wpisz kod
   suffix = "am"
elif hour < 12:
   suffix ="am"
    # Co rano?
elif hour == 12:
    # Co w południe?
    suffix = "pm"
else:
    # Co po południu (godziny 13-23)?
    hour = hour - 12
    suffix = "pm"
    pass

# Krok 4: Wypisanie wyniku
print(f"Time in 12-hour format: {hour}:{minute_str}{suffix}")