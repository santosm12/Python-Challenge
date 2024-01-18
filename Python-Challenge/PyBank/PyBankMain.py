import os

import csv
data = []

csvpath = os.path.join('.','Python-Challenge','Pybank','Resources','budget_data.csv')

text_path = "results.txt"

with open('budget_data.csv') as file:
    
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        print(row)
        data.append(row)
        print(data)


column_index = 1
sum_value = 0

for row in data:
    row[column_index] = int(row[column_index])
    sum_value += row[column_index]

print("Total:", sum_value) 

changes = []
previous_profit = int(data[0][1])
for row in data[1:]:
    current_profit = int(row[1])
    change = current_profit - previous_profit
    changes.append(change)
    previous_profit = current_profit

average_change = sum(changes) / len(changes)

print(f"Average Change: ${average_change:.2f}")


column_index = 0
counter = 0

for row in data:
    row[column_index] != ""
    counter += 1
print("Total Months:", counter)

column_index = 1
max_value_index = 0
max_increase = 0 

for i in range(1, len(data)):
    current_value = int(data[i][column_index])
    previous_value = int(data[i-1][column_index])
    increase = current_value - previous_value
    if increase > max_increase:
        max_increase = increase
        max_increase_index = i

print("Greatest Increase in Profits:", data[max_increase_index][0], "($", max_increase, ")")

column_index = 1
max_decrease = 0
max_decrease_index = 0

for i in range(1, len(data)):
    current_value = int(data[i][column_index])
    previous_value = int(data[i-1][column_index])
    decrease = previous_value - current_value
    if decrease > max_decrease:
        max_decrease = decrease
        max_decrease_index = i

print("Greatest Decrease in Profits:", data[max_decrease_index][0], "($", max_decrease, ")") 

with open("results.txt", "w") as file:
    file.write("Total Months: " + str(counter) + "\n")
    file.write("Total: " + str(sum_value) + "\n")
    file.write("Average Change: " + str(average_change) + "\n")
    file.write("Greatest Increase: " + str(max_increase) + "\n")
    file.write("Greatest Decrease: " + str(max_decrease) + "\n")
