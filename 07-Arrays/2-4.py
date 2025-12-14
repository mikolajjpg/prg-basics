#Poniższe dane zawierają tygodniowy plan posiłków.
#Napisz program,
#który drukuje tygodniowy plan posiłków wraz z nazwą dnia, jak w poniższym przykładzie.

#WEEKLY MEAL PLAN
#(Breakfast, Lunch, Dinner)
#==========================
#Monday: Oatmeal, Grilled Checken Salad, Spaghetti
#Tuesday: ...
#Wednesday: ...

# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   weekday_counted = weekdays[n-1]
   return weekday_counted

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
    return ", ".join(meal_plan[day_number-1])
            


        



                


# Prints weekly meal plan
if __name__ == "__main__":
    print("WEEKLY MEAL PLAN")
    print("(Breakfast, Lunch, Dinner)")
    print("==========================")
    for i in range(1,8):
        print( f'{weekday(i)}: {day_meal_plan(meal_plan,i)}' )
    