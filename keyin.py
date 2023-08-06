import re

with open('Data.txt', 'r') as file:
    data = file.readlines()

for line in data:
    line.strip("\n")
issues = [line.strip("\n") for line in data]

issues = ",".join(issues)
print(issues)

with open('Data_out_2.txt', 'w') as file:
    file.writelines(issues)