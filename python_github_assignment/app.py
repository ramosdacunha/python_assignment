#simple study time tracker program
print("Welcome to my Python program!")
hours = float(input("How many hours did you study today? ")) #ask user for input

#handle invalid input
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
#estimate weekly study time
weekly_hours = hours * 7
#Display result
print(f"You are on track to study {weekly_hours} hours this week.")