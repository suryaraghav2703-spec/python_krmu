# Project:- Daily Calorie Tracker CLI
# made by:- Surya Pratap singh
# Roll no.:- 2501730038
# submission Date:- 10 Nov 2025

import datetime

print("=======================================")
print(" Welcome to Daily Calorie Tracker CLI ")
print("Track your meals, calories, and live healthy!")
print("=======================================\n")

# step 2: Input & Data Collection
meals = []
calories = []

meal_count = int(input("How many meals do you want to enter today? "))

for i in range(meal_count):
    meal_name = input(f"\nEnter name of meal #{i+1}: ")
    cal = float(input(f"Enter calories for {meal_name}: "))
    
    meals.append(meal_name)
    calories.append(cal)

# step 3: Calorie Calculations
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# step 4: Exceed Limit Warning System
if total_calories > daily_limit:
    status = "You have exceeded your daily calorie limit!"
else:
    status = "Great job! You are within your daily calorie limit."

# step 5:  Output which will come
print("\n========== DAILY CALORIE REPORT ==========")
print("Meal Name\tCalories")
print("------------------------------------------")
for i in range(meal_count):
    print(f"{meals[i]:<15}\t{calories[i]}")
print("------------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print("------------------------------------------")
print(status)
print("==========================================\n")

# step 6: Save Session(in .txt file)
save = input("Do you want to save this session? (yes/no): ").strip().lower()

if save == "yes":
    filename = "calorie_log.txt"
    with open(filename, "a") as file:  # ← "a" means append (add new report below old ones)
        file.write("\n\n===== DAILY CALORIE TRACKER REPORT =====\n")
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("------------------------------------------\n")
        for i in range(meal_count):
            file.write(f"{meals[i]:<15}\t{calories[i]}\n")
        file.write("------------------------------------------\n")
        file.write(f"Total:\t\t{total_calories}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        file.write(f"Status:\t\t{status}\n")
        file.write("==========================================\n")

    print(f"\nSession successfully saved to '{filename}' (added to history).")

print("\nThank you for using Daily Calorie Tracker CLI! Stay healthy!")