import csv
from datetime import datetime
today = datetime.today()
try:
    with open("maintenance.csv", "r") as file:
        reader = csv.DictReader(file)
        print("Overdue maintenance tasks:\n")
        for row in reader:
         due_date = datetime.strptime(row["due_date"], "%d-%m-%Y")
         if due_date < today and row["Status"]== "Pending":
                print(f" Aircraft: {row['Aircraft']}")
                print(f"task: {row['Task']}")
                print(f"due_date: {row['due_date']}")
                print("-"*30)
                found_task =True
    if not found_task:
         print("all task are completed")

except FileNotFoundError:
    print("Error: maintenance.csv file not found!")
except KeyError as e:
    print(f"Error: Missing column {e} in CSV file")