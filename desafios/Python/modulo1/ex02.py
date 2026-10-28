minute = int(input("Enter the number of minutes: "))
hours = minute // 60
remaining_minutes = minute % 60
print(f"{minute} minutes is equal to {hours} hours and {remaining_minutes} minutes.")